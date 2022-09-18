<template>
    <div>
        <h1> 主页组件Home</h1>
        <img alt="item" src="../assets/3.png" width="800">

        <!-- <div style="width: 100%;height: 300px;background:red;">数据内容</div> -->
        <!-- 使用组件 -->
        <Footer></Footer>
    </div>
</template>
  
<script>
  import Footer from "./Footer" //引入组件
  export default {
    name: 'Home',
    components: {
        Footer,//注册组件
    }
  }
</script>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
  