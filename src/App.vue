<template>
  <div id="app">

    <el-menu
      :default-active="$route.path"
      router
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
      <el-menu-item index="/community">
        <span slot="title">社区</span>
      </el-menu-item>
      <el-menu-item index="/group">
        <span slot="title">圈子</span>
      </el-menu-item>
      <el-menu-item index="/post">
        <span slot="title">帖子</span>
      </el-menu-item>
      <!-- <el-submenu index="/profile">
        <template slot="title">好友列表</template>
        <el-menu-item v-for="(item, index) in friends" index=index>
          <a href="javascript:void(0)" onclick="toInfo(item.userId)" >{{item.name}}</a>
        </el-menu-item>
      </el-submenu> -->
      <el-menu-item index="/Activity">
        <i class="el-icon-menu"></i>
        <span>活动</span>
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
    data() {
      return {
        friends:[
          {
            "userId" : 1,
            "name" : "zlb",
            "pic" : "url",
          },
          {
            "userId" : 2,
            "name" : "ghy",
            "pic" : "url",
          },
          {
            "userId" : 3,
            "name" : "zal",
            "pic" : "url",
          }
        ]
      }
    },
    methods:{
      toInfo(id){
        console.log(id)
        this.$store.commit("setOtherid",id)
        this.$router.push('/profile')
      },
      getFriendsList(){
        console.log("yes")
        this.$http({
              method: 'post',
              url: '/getFriendsList',
              data: qs.stringify({
                userId:this.$store.state.user_id
              })
          }).then((res) => {
              console.log(res.data)
              this.friends = res.data.friends;
          })
      },
      
      handleSelect(key, keyPath) {
        console.log(key);
        this.$router.push(keyPath)
      }
    }
  }
</script>

<style lang="scss">
  .aa{
    background-color: red;
  }
</style>
