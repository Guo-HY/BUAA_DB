<template>
    <div>
      <el-container>
        <el-header>
          <img class="logoimg" src="../../assets/makefun.png" alt=""></img>
          <el-row type="flex" class="row-bg" justify="center">
            <el-col :span="14">
              <p class="introw">makeFun社交平台是基于部分匿名消息和兴趣图谱的属于当代大学生的虚拟社交平台。在makeFun中用户可以无顾虑的表达自己,认知他人,交流兴趣和观点,获得精神共鸣和认同感。在交流中获取信息,并获得有质量的新关系。在元宇宙带来的社交新浪潮下,makeFun展现真实,有趣,温暖的社交面貌,致力于满足当代大学生的精神需求。
同时,makeFun还相信大众的力量,多数人的判断,和数字的智慧。所有的内容,分类,筛选,排序都由每一个用户决定和产生。在makeFun的社区中,给评论一个赞,它的排位会自动上升。贴一个tag给一个圈子,它会在整个网站的标签分类中出现。</p>
            </el-col>
          </el-row> 
        </el-header>
        <el-main>
          <el-col :span="6">
            <img class="loveimg" src="../../assets/love.png" alt=""></img>
          </el-col>
          <el-col :span="4">
            <img class="arrowimg" src="../../assets/arrow.png" alt=""></img>
          </el-col>
          <el-col :span="14">
            <p class="lovew">
              有人在这儿走进了爱情的怀抱
            </p>
          </el-col>
        </el-main>
      </el-container>
      
      
      
      
      
      
      <!-- <h1> 主页组件Home</h1>
        <img alt="item" src="../../assets/3.png" width="100%"> -->

        <!-- <div style="width: 100%;height: 300px;background:red;">数据内容</div> -->
        <!-- 使用组件 -->
        <!-- <Footer></Footer> -->
        <dialog-component v-show="Visiable" ref="dialog"></dialog-component>
    </div>
</template>
  
<!-- <script>
  import Footer from "./Footer" //引入组件
  export default {
    name: 'Home',
    components: {
        Footer,//注册组件
    }
  }
</script> -->


<script>
import dialogComponent from "./PopupInHome";
export default {
  name: "Home",
  components: {dialogComponent},
  props: {},
  data() {
    return {
      Visible:false,
      imgList: [
        {id:0,idView:'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg'},
        {id:1,idView:'https://fuss10.elemecdn.com/1/34/19aa98b1fcb2781c4fba33d850549jpeg.jpeg'},
        {id:2,idView:'https://fuss10.elemecdn.com/0/6f/e35ff375812e6b0020b6b4e8f9583jpeg.jpeg'},
        {id:3,idView:'https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg'},
        {id:4,idView:'https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg'},
        {id:5,idView:'https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg'},
        {id:6,idView:'https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg'},
      ]
    };
  },
  watch: {},
  computed: {},
  methods: {
    //函数防抖
    debounce(func, wait) {
        let timeout;
        return function () {
            let context = this;
            let args = arguments;
            if (timeout) clearTimeout(timeout);
            timeout = setTimeout(() => {
                func.apply(context, args)
            }, wait);
        }
    },
    //判断滚动方向
    handleScroll(e){
      console.log(e)
        let direction = e.deltaY > 0 ? 'down' : 'up'
        if (direction == 'down') {
          this.Visible=true
          this.$nextTick(()=>{
          //这里的dialog与上面dialog-component组件里面的ref属性值是一致的
          //init调用的是dialog-component组件里面的init方法
          //data是传递给弹窗页面的值
            // console.log(this.$refs);
            this.$refs.dialog.init(this.Visible);
          })
        }
    },
  },
  created() {},
  mounted() {//监听鼠标滚动事件
    window.addEventListener('mousewheel', this.debounce(this.handleScroll,300), true)||window.addEventListener("DOMMouseScroll",this.debounce(this.handleScroll,300),false)
  },
};
</script>

<style lang="scss" scoped>
.logoimg{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 800px;
  margin: 100px 430px 0;
}

.introw{
  font-family:Georgia, 'Times New Roman', Times, serif;
  font-size: 20px;
  letter-spacing:5px;
  line-height: 1.8
}

.loveimg{
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 350px;
  margin: 650px 220px 0;
}

.arrowimg{
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 200px;
  margin: 800px 300px 0;
}

.lovew{
  font-family:Georgia, 'Times New Roman', Times, serif;
  font-size: 22px;
  letter-spacing:3px;
  line-height: 1.8;
  margin: 860px 300px 0;
}
</style>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<!-- <style scoped>
  
</style> -->
  