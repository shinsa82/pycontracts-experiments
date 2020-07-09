# pycontracts-experiments

Experiments on PyContracts

## Setup

I use pyenv (of anyenv) and miniconda:

```bash
pyenv virtualenv miniconda3-latest pycontracrts
pyenv local pycontracts
conda install -y pytest autopep8
pip install PyContracts
```

> `autopep8` is used by VSCode to format source.

At the time of writing, the following libraries are installed by the commands above:

- python: 3.8.3
- pytest: 5.4.3
- PyContracts: 1.8.12

The created conda env can be directly activated by `pyenv activate pycontracts`.
You may need to execute `pyenv rehash` to set PATH correctly.

## 基本的な使い方

コントラクトをメソッドのデコレータで指定する。
コントラクトの内容はデコレータの引数として渡すか、メソッド定義の型ヒントとして与える:

デコレータ引数の例:

```python
@contract(a=int, l='list[N]', returns='list[N+1]')
def prepend(a, l):
    l.insert(0, a)
    return l
```

型ヒントの例:

```python
@contract
def pos_add(a: 'int,>0', b: int):
    return a+b
```

プログラム自体は普通に実行すればよい。コントラクトを満たさない場合には例外 (この場合は ContractNotRespected) が発生する。

```shell
[04:06:23 ~/git/work-2020/pycontracts-experiments] (master)$ python sample.py 
Traceback (most recent call last):
  File "sample.py", line 27, in <module>
    l = prepend(3, [2, 1, 4])
  File "<decorator-gen-3>", line 2, in prepend
  File "/Users/shinsa/.anyenv/envs/pyenv/versions/pycontracts/lib/python3.8/site-packages/contracts/main.py", line 279, in contracts_checker
    raise e
  File "/Users/shinsa/.anyenv/envs/pyenv/versions/pycontracts/lib/python3.8/site-packages/contracts/main.py", line 274, in contracts_checker
    returns_parsed._check_contract(context, result, silent=False)
  File "/Users/shinsa/.anyenv/envs/pyenv/versions/pycontracts/lib/python3.8/site-packages/contracts/interface.py", line 452, in _check_contract
    self.check_contract(context, value, silent)
  File "/Users/shinsa/.anyenv/envs/pyenv/versions/pycontracts/lib/python3.8/site-packages/contracts/library/lists.py", line 20, in check_contract
    self.length_contract._check_contract(context, len(value), silent)
  File "/Users/shinsa/.anyenv/envs/pyenv/versions/pycontracts/lib/python3.8/site-packages/contracts/interface.py", line 452, in _check_contract
    self.check_contract(context, value, silent)
  File "/Users/shinsa/.anyenv/envs/pyenv/versions/pycontracts/lib/python3.8/site-packages/contracts/library/simple_values.py", line 19, in check_contract
    raise ContractNotRespected(contract=self, error=error,
contracts.interface.ContractNotRespected: Breach for return value of prepend().
EqualTo: Condition 5 == 4 not respected.
checking: N+2         for value: Instance of <class 'int'>: 4               
checking: list[N+2]   for value: Instance of <class 'list'>: [3, 2, 1, 4]   
Variables bound in inner context:
- N: Instance of <class 'int'>: 3
```
