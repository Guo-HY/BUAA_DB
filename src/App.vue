<template>
  <div id="app">
    <a href="#/home">Home组块</a> 
    <a href="#/user">用户模块</a>
    <a href="#/student">学生模块</a>
    <!-- 用来展示路由组件 -->
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'App',
   
  }
</script>

<style lang="scss">
  .aa{
    background-color: red;
  }
</style>
