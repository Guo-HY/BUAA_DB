<template>
  <div class="container">
        <img src="../assets/bg.jpg" alt="">
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
.loginbox{
  display:flex;
  position:absolute;
  width:800px;
  height:400px;
  top:40%;
  left:50%;
  transform:translate(-50%,-50%);
  box-shadow: 0 12px 16px 0  rgba(0,0,0,0.24), 0 17px 50px 0 #4E655D;
}
.loginbox-in{
  background-color:#1aaba8;
  width:280px;
}
.idbox{
  margin-top:120px ;
  height:30px;
  width:230px;
  display: flex;
  margin-left:25px;
}
.pwdbox{
  height:30px;
  width:225px;
  display: flex;
  margin-left:25px;
}

.background{
  width:450px;
  background-image:url('./img/在线教学平台.png');
  background-size:cover;
  font-family:sans-serif;
}
.title{
  margin-top:320px;
  font-weight:bold;
  font-size:20px;
  color:#4E655D;

}
.title:hover{
  font-size:21px;
  transition: all 0.4s ease-in-out;
  cursor: pointer;
}
.uesr-text{
  position:left;
}
input{
  outline-style: none ;
  border: 0;
  border-bottom:1px solid #E9E9E9;
  background-color:transparent;
  height:20px;
  font-family:sans-serif;
  font-size:15px;
  color:#445b53;
  font-weight:bold;
}
/* input::-webkit-input-placeholder{
   color:#E9E9E9;
} */
input:focus{
  border-bottom:2px solid #445b53;
  background-color:transparent;
  transition: all 0.2s ease-in;
  font-family:sans-serif;
  font-size:15px;
  color:#445b53;
  font-weight:bold;

}
input:hover{
  border-bottom:2px solid #445b53;
  background-color:transparent;
  transition: all 0.2s ease-in;
  font-family:sans-serif;
  font-size:15px;
  color:#445b53;
  font-weight:bold;

}

input:-webkit-autofill {
  /* 修改默认背景框的颜色 */
  box-shadow: 0 0 0px 1000px  #89AB9E inset !important;
  /* 修改默认字体的颜色 */
  -webkit-text-fill-color: #445b53;
}

input:-webkit-autofill::first-line {
  /* 修改默认字体的大小 */
  font-size: 15px;
  /* 修改默认字体的样式 */
  font-weight:bold;
}
.log-box{
  font-size:12px;
  display: flex;
  justify-content: space-between ;
  width:190px;
  margin-left:30px;
  color:#4E655D;
  margin-top:-5px;
  align-items: center;

}
.log-box-text{
  color:#4E655D;
  font-size:12px;
  text-decoration:underline;
}
.login_btn{
  background-color: #5f8276; /* Green */
  border: none;
  color: #FAFAFA;
  padding: 5px 22px;
  text-align: center;
  text-decoration: none;
  font-size: 13px;
  border-radius: 20px;
  outline:none;
}
.login_btn:hover{
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  cursor: pointer;
  background-color: #0b5137;
  transition: all 0.2s ease-in;
}

.warn{
  margin-top:60px;
  /* margin-right:120px; */
  margin-left:-120px;
  margin-bottom: 5px;
  font-weight:bold;
  font-size:17px;
}

.register_btn{
  background-color: transparent; /* Green */
  border: none;
  text-decoration: none;
  font-size: 12px;
  /* border-radius: 20px;   */
  color:#4E655D;
  font-size:12px;
  text-decoration:underline;
  display: flex;
  margin-left:25px;
  outline:none;

}
.register_btn:hover{
  font-weight:bold;
  cursor: pointer;
}
@font-face {
  font-family: "iconfont";
  src: url('./font/iconfont.eot');
  src: url('./font/iconfont.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
  url('./font/iconfont.woff2') format('woff2'), url('./font/iconfont.woff') format('woff'), url('./font/iconfont.ttf') format('truetype'), /* chrome, firefox, opera, Safari, Android, iOS 4.2+ */
  url('./font/iconfont.svg#iconfont') format('svg');
}

.iconfont {
  font-family: "iconfont" !important;
  font-size: 20px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height:22px;
  color:#4E655D;
  margin-right:10px;
  margin-top:3px;
}

.icon-key:before {
  content: "\e775";
}

.icon-account:before {
  content: "\e817";
}





</style>