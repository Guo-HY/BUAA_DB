<template>
  <div class="container">
        <img src="../assets/m.jpeg" alt="">
        
        <div class="panel">
            <div class="content login">
                <div class="switch">
                    <span :class='{"active":active === "login"}' @click="go('login')">登录</span>
                    <span>/</span>
                    <span :class='{"active":active === "register"}' @click="go('register')">注册</span>
                </div>
                <div class="form" id="fromLogin">
                    <!-- 如果按钮选择的是注册就展示这个里面的内容 -->
                    <template v-if="active === 'register'">
                        <div class="input">
                            <input :class="{hasValue : registerForm.name}" v-model="registerForm.name" type="text" name="name" id="name">
                            <label for="email">用户名</label>
                        </div>
                        <div class="input">
                            <input :class="{hasValue : registerForm.password}" v-model="registerForm.password" type="text" name="password" id="password">
                            <label for="email">密码</label>
                        </div>
                        <div class="input">
                            <input :class="{hasValue : registerForm.contact}" v-model="registerForm.contact" type="text" name="contact" id="contact">
                            <label for="email">联系方式</label>
                        </div>
                        <div class="input">
                            <input :class="{hasValue : registerForm.age}" v-model="registerForm.age" type="text" name="age" id="age">
                            <label for="email">年龄</label>
                        </div>
                        <div class="input">
                            <input :class="{hasValue : registerForm.gender}" v-model="registerForm.gender" type="text" name="gender" id="gender">
                            <label for="email">性别</label>
                        </div>
                        <div class="input">
                            <input :class="{hasValue : registerForm.address}" v-model="registerForm.address" type="text" name="address" id="address">
                            <label for="email">住址</label>
                        </div>
                        <div class="input">
                            <input type="file" @change="getImageFile" id="img">
                            <label for="email">上传头像</label>
                        </div>
                        <button type="submit" @click="submit" >注册</button>
                    </template>
                    <!-- 如果按钮选择的是登录就展示这个里面的内容 -->                
                    <template v-if="active === 'login'">
                        <div class="input">
                            <input :class="{hasValue : loginForm.name}" v-model="loginForm.name" type="text" name="name" id="name">
                            <label for="email">用户名</label>
                        </div>
                        <div class="input">
                            <input :class="{hasValue : loginForm.password}" v-model="loginForm.password" type="text" name="password" id="password">
                            <label for="email">密码</label>
                        </div>
                        <span>忘记密码?</span>
                        <button type="submit" @click="submit" >登录</button>
                    </template>
                    
                </div>
            </div>
        </div>
    </div>
</template>


<!-- major改gender,换成下拉列表 -->
<!-- 还有一堆要补充的信息 -->

<script>
import qs from "qs"
export default {
  name: "Login",
  props:{
  },
  data() {
    return {
      active :'login',
            registerForm:{
                name : '',
                password : '',
                contact : '',
                age : '',
                gender : '',
                address : '',
                img : ''
            },
            loginForm :{
                name : '',
                password : ''
            },
            dis:false
            
    };
  },

  methods:{
    getImageFile:function(e) {
        let file = e.target.files[0];
        this.registerForm.img = file;
      },
    go(type){
        this.active = type;
    },
    ifDis(){
      if ((this.active == 'register' &&(this.registerForm.name == '' || this.registerForm.password == '' || this.registerForm.contact == '' || this.registerForm.age == '' || this.registerForm.gender == '' || this.registerForm.address == '')) || (this.active=='login'&&(this.loginForm.name == '' || this.loginForm.password == ''))) {
          return true;
      }
      return false;
    },
    submit(){
        console.log(this.active)
        // console.log(this.registerForm)
        // console.log(this.loginForm)

        // console.log(Dis)
        // if ((this.active == 'register' &&(this.registerForm.name == '' || this.registerForm.password == '' || this.registerForm.contact == '' || this.registerForm.age == '' || this.registerForm.gender == '' || this.registerForm.address == '')) || (this.active=='login'&&(this.loginForm.name == '' || this.loginForm.password == ''))) {
        //   this.dis = true;
        // }
        // else {
          if(this.active === 'login'){
            this.$http({
                method: 'post',
                url: '/api/userLogin',
                data: qs.stringify({
                  name:this.loginForm.name,
                  password: this.loginForm.password
                })
            }).then((res) => {
                console.log(res.data.status)
                console.log(res.data.userId)
                if (res.data.status == 'not_found'){
                  alert("用户不存在,请先注册哦!"); 
                }
                else if (res.data.status == 'password_wrong'){
                  alert("密码错误,请重新输入密码"); 
                }
                else {
                  // 后端向前端返回user_id
                  this.$store.commit("setUser", res.data.userId)
                  console.log(this.$store.state.user_id)
                  // 跟张爱玲一致
                  this.$router.push('/UserInfo')
                }
                
            })
          } 
          if  (this.active === 'register'){
            let formData = new FormData();
            formData.append('name', this.registerForm.name);
            formData.append('password', this.registerForm.password);
            formData.append('contact', this.registerForm.contact);
            formData.append('age', this.registerForm.age);
            formData.append('gender', this.registerForm.gender);
            formData.append('address', this.registerForm.address);
            formData.append('pic', this.registerForm.img);
            this.$http({
                method: 'post',
                url: '/api/userRegister',
                data:formData
                // data: qs.stringify({
                //   name:this.registerForm.name,
                //   password: this.registerForm.password,
                //   contact : this.registerForm.contact,
                //   age : this.registerForm.age,
                //   gender : this.registerForm.gender,
                //   address : this.registerForm.address
                // })
            }).then((res) => {
                console.log(res.data.status)
                if (res.data.status == 'name has an account registered. please log in.'){
                  alert("同学你已经注册过帐号啦,直接登录吧!"); 
                }
                else if (res.data.status == 'unknown_fail') {
                  alert("未知错误!")
                }
                else {
                  alert("注册成功,请登录吧~");
                  this.$router.go(0);
                }
            })
          }
          // this.$router.go(0)
        // }
    },
    mounted(){
    //   this.dis = (this.active == 'register' &&(this.registerForm.name == '' || this.registerForm.password == '' || this.registerForm.contact == '' || this.registerForm.age == '' || this.registerForm.gender == '' || this.registerForm.address == '')) || (this.active=='login'&&(this.loginForm.name == '' || this.loginForm.password == ''))
    },
    computed:{
      Dis:function(){
        return (this.active == 'register' &&(this.registerForm.name == '' || this.registerForm.password == '' || this.registerForm.contact == '' || this.registerForm.age == '' || this.registerForm.gender == '' || this.registerForm.address == '')) || (this.active=='login'&&(this.loginForm.name == '' || this.loginForm.password == ''))
      }
    }
  }


}
</script>

<style scoped src="../assets/css/style.css">

</style>