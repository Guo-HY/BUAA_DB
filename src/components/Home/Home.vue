<template>
    <div>
        <h1> 主页组件Home</h1>
        <img alt="item" src="../../assets/3.png" width="100%">

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
      Visible:false
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

</style>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<!-- <style scoped>
  
</style> -->
  