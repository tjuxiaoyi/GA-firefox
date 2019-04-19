# GA-firefox<br/>
本代码用100个半透明三角形生成火狐图标。<br/>
参考[代码仓库](https://github.com/TuanZ7/GA-Firefox-)<br/>
参考[文章](https://songshuhui.net/archives/10462)<br/>

实验参数设置：<br/>
    种群大小 ： 16<br/>
    变异率  :  0.1<br/>
    交叉率 : 0.86<br/>
    选择方式 ： 每次淘汰fitness最低的两条染色体 用fitness最高的两条染色体的交叉替换<br/>
    
实验效果：
本人实验在20000轮后陷入局部最优，最后得到的效果仅有模糊轮廓。<br/>
实验中为保证实验速度，设置图像大小为32*32，但是本人写的代码还是很慢，接近24小时才跑了20000轮.<br/>
据上述参考文章中作者在评论区介绍，他的代码仅用半小时即可演化1800000轮，并且效果非常好，如果有了解怎么优化的大佬看到我的代码，恳请指教。<br/>
实验结果如下图：<br/>
![Aaron Swartz](https://github.com/tjuxiaoyi/GA-firefox/blob/master/experimentResult.png)
