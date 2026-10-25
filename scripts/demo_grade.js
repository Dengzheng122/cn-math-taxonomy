#!/usr/bin/env node
/* 整年级 / 整册诊断演示：node scripts/demo_grade.js [一年级|七上] [limit] [seed]
 * 用真实 data/*.json，模拟一位学生（约 1/6 的知识点不会、1/6 不稳，其余会），跑一遍筛查并打印按章汇总。 */
'use strict';
const fs = require('fs');
const path = require('path');
const E = require('../diagnose/engine.js');

const dir = path.join(__dirname, '..', 'data');
const read = (f) => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
const G = E.buildGraph(read('topics.json'), read('dependencies.json'), read('questions.json'));

const scope = process.argv[2] || '七年级';
const limit = process.argv[3] ? parseInt(process.argv[3], 10) : undefined;
const seed = process.argv[4] || 'demo';
const g = E.gradeTargets(G, scope);
if (!g) { console.error('不认识的范围：' + scope + '（写法如 一年级 / 七上）'); process.exit(1); }

const oracle = (id, attempt) => {
  const i = G.index[id];
  if (i % 6 === 0) return 'wrong';
  if (i % 6 === 3) return attempt === 1 ? 'wrong' : 'correct';
  return 'correct';
};

let s = E.createSession(G, g.ids, { mode: 'screen', limit, seed });
for (let n = 0; n < 1000; n++) {
  const it = E.nextItem(G, s);
  if (!it) break;
  s = E.applyAnswer(G, s, it.topicId, oracle(it.topicId, it.attempt));
}
const sum = E.summarize(G, s);
const name = (id) => G.byId[id].name;
console.log(g.label + '：' + g.ids.length + ' 个知识点，题量上限 ' + s.limit + '，实际答 ' + sum.asked + ' 题' + (sum.limitReached ? '（到上限）' : '（问完）'));
console.log('掌握 ' + sum.mastered.length + ' / 不稳 ' + sum.shaky.length + ' / 薄弱 ' + sum.weak.length + ' / 未测 ' + sum.untested.length + '；根因 ' + sum.roots.length + ' 个\n');
E.chapterSummary(G, s).forEach((c) => {
  console.log(c.label + '  共 ' + c.total + '：掌握 ' + c.mastered + ' 不稳 ' + c.shaky + ' 薄弱 ' + c.weak + ' 未测 ' + c.untested +
    (c.weakIds.length ? '\n    薄弱：' + c.weakIds.map(name).join('、') : ''));
});
