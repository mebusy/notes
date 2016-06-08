...menustart

 * [github](#bf215181b5140522137b3d4f6b73544a)
	 * [github update fork](#f6b73a9a864f02b2d14ad454c6b09e68)

...menuend


<h2 id="bf215181b5140522137b3d4f6b73544a"></h2>
# github 

<h2 id="f6b73a9a864f02b2d14ad454c6b09e68"></h2>
## github update fork

 - 给fork配置远程上游仓库 
    - `git remote add upstream xxxx.git`
 - 同步fork
    - 从上游仓库 fetch 分支和提交点，提交给本地 master，并会被存储在一个本地分支 upstream/master 
        - `git fetch upstream` 
    - 切换到本地主分支(如果不在的话) 
        - `git checkout master` 
    - 把 upstream/master 分支合并到本地 master 上，这样就完成了同步，并且不会丢掉本地修改的内容。
        - `git merge upstream/master` 
    - 提交 
        - `git push origin master`

        
