<template>
  <div>
      <h2>用户添加信息</h2>
      <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="用户名">
          <el-input v-model="user.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="年龄">
          <el-input v-model="user.age" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="生日" prop="age">
          <el-input v-model="user.bir"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="saveUserInfo">提交</el-button>
        </el-form-item>
      </el-form>

      <!-- <form action="">
        用户名: <input v-model="user.name" type="text"><br> 
        年龄: <input v-model="user.age" type="text"><br>
        生日: <input v-model="user.bir" type="text"><br>
        <input type="button" @click="saveUserInfo" value="添加用户信息">
      </form> -->
  </div>
</template>

<script>
import router from '@/router/index.js'
import User from '@/components/User'
export default {
  name: "UserAdd",
  components: {},
  props: {},
  data() {
    return {
      user: {}
    };
  },
  watch: {},
  computed: {},
  methods: {
    saveUserInfo(){
      // const self = this
      // console.log(this.user)
      // 发送axios请求
      this.$http.post("http://rap2api.taobao.org/app/mock/306658/http/user/add", this.user).then(res=>{
        console.log(res.data.success);
        if (res.data.success){
          this.$router.push("/user") // 切换路由
        }
      })
    }
  },
  created() {},
  mounted() {}
};
</script>

<style lang="scss" scoped>

</style>