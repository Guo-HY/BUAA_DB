<template>
    <div>
      <el-carousel :interval="4000" type="card" height="200px">
        <el-carousel-item v-for="item in imgList" :key="item.id">
          <img :src="item.idView" class="image">
        </el-carousel-item>
      </el-carousel>
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
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}
</style>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<!-- <style scoped>
  
</style> -->
  