# codex-demo

用于验证 Codex 与 GitHub 的 PR 集成链路（分支 → 提交 → PR → 关联到任务）。

## 结构

- `hello.py` — 最小示例脚本

## 使用

```bash
python hello.py
python hello.py 你的名字
python hello.py -u
python hello.py -u Alice Bob
```

## 参数

- 位置参数：要问候的名字，可传多个；不传则使用 `world`
- `-u`, `--upper`：把问候语转成大写
