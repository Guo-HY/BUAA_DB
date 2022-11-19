<template>
  <el-container>
    <el-header class="makeFun">
      MakeFun
    </el-header>
    <el-container style="height: 500px; border: 1px solid #eee">
      <el-aside>
        <el-menu
            background-color="#30B7A5"
            text-color="#fff"
            default-active="1"
            class="el-menu-vertical-demo"
            router="true">
          <el-menu-item index="/">
            <i class="el-icon-location-information"></i>
            <span>主页</span>
          </el-menu-item>
          <el-menu-item index="/Activity">
            <i class="el-icon-menu"></i>
            <span>活动</span>
          </el-menu-item>
          <el-menu-item index="/Community">
            <i class="el-icon-coordinate"></i>
            <span>社区</span>
          </el-menu-item>
          <el-menu-item index="/DriftBottles">
            <i class="el-icon-coffee"></i>
            <span>漂流瓶</span>
          </el-menu-item>
          <el-menu-item index="/UserInfo">
            <i class="el-icon-document"></i>
            <span>个人资料</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view>
        </router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #30B7A5;
}

.navigation{
  height: 200px;
}
.makeFun{
  height: 100px;
}
</style>
