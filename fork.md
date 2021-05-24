# fork について
### 既存の remote repo から作成する(**fork**)
 - **fork** することで、自分の remote repo に fork したproject repo のコピーを作ることができる
    - 本家の repo には影響を与えずに作業できる
    - 本家の repo に pull request を送ることも可能
    - open source project の開発の時にもよく使う
1.  開発に携わりたい project があった
2.  fork して 自身の remote repo にその project repo の repo を作成
3.  fork → 自身の remote repo(project repo fork) を clone して loacl repo 作成
4.  ある程度完成してきたら、本家に pull request を出して merge してもらう
### fork してみる！
- この D-S-hub はかめさんが運営しているコミニティー
> https://github.com/D-S-Hub/git-practice
- edit を使う良い練習になる
1. D-S-Hub へ acssce
2. fork bouttn を押して、自分の remote repo へ copy 作成
> fork bouttn を押した後は、勝手に自分の remote repo と紐づいて、元のfork した repo とは独立した自分自身 remote repo になり、自由に開発・編集可能なものになる。
#### 「 元の remote repo (forkしたrepo)に影響を与える事はない 」
3. git clone<url>で、loacl repo に clone する
- ここで気おつける事は、fork 元 を clone するのではなく、自分自身が fork して作成した remote repo を clone する事！！
#### clone
    git clone git@github.com:github user name/git-practice.
4. local で開発して 自身の remote repo へ
5. 完成したら、自身の remote repo から fork 元へ pull request を出して merge してもらう
