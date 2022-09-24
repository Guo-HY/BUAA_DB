<template>
  <div id="app">

    <el-menu
      :default-active="this.$router.path"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      router>
      <el-menu-item index="/home">
        <span slot="title">Home组块</span>
      </el-menu-item>
      <el-menu-item index="/user">
        <span slot="title">用户模块</span>
      </el-menu-item>
      <el-menu-item index="/student">
        <span slot="title">学生模块</span>
      </el-menu-item>
      <el-menu-item index="/chooseclass">
        <span slot="title">选择课程</span>
      </el-menu-item>
    </el-menu>

    <!-- <a href="#/home">Home组块</a> 
    <a href="#/user">用户模块</a>
    <a href="#/student">学生模块</a> -->
    
    <!-- <el-link type="primary" href="#/home">Home组块</el-link>
    <el-link type="success" href="#/user">用户模块</el-link>
    <el-link type="warning" href="#/student">学生模块</el-link> -->
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
