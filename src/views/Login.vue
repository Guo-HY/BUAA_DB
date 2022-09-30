<template>
  <div class="container">
    <div class="main">
      <!-- 整个注册盒子 -->
      <div class="loginbox">
        <!-- 左侧的注册盒子 -->
        <div class="loginbox-in">
          <div class="idbox">
            <span class="iconfont">&#xe817;</span>
            <input  class="id" id="id"   v-model="name" placeholder="学号">
          </div>
          <br>
          <div class="pwdbox">
            <span class="iconfont">&#xe775;</span>
            <input  class="pwd" id ="password" type="password"  v-model="pwd" placeholder="密码">
          </div>
          <br>
          <div class="log-box">
            <div class="log-box-text"> 忘记密码</div>
            <button type="primary"  class="login_btn" @click="login_e">Login</button>
          </div>

          <br>
          <div class="warn">@buaa</div>
          <button type="primary"  class="register_btn" @click="register">若无账号请点击注册</button>
        </div>

        <!-- 右侧的注册盒子 -->
        <div class="background">
          <div class="title">欢迎来到选课系统</div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import qs from "qs";

export default {
  name: "Login",

  data:function (){
    return{
      name:'',
      pwd:'',
      user_list:[
        {
          id:'1',
          username:'admin',
          password:'123',
          grade:'',
          classId:'',
        },
      ]

    }
  },

  methods:{

    register(){  this.$router.push("Register")},

    // getParams: function () {
    //         // 取到路由带过来的参数
    //         var routerParams = this.$route.query.list;
    //         this.user_list = routerParams;
    // },

    login_e(){
      if(this.name==''||this.pwd=='') {
        alert("请填写完整！");
        return;
      }
      this.$axios({
        method: 'post',
        url: '/api/studentLogin',
        data: qs.stringify({
          student_id: this.id,
          student_password: this.pwd
        })
      }).then(res => {              /* res 是 response 的缩写 */
        switch (res.data.status) {
          case "success":
            alert("注册成功！");
            this.$router.push({
                  path: 'Homepage',
                }
            )
            break;
          case "student_id_not_found":
            alert("该学号不存在");
            break;
          case "student_password_wrong":
            alert("用户名或密码错误，请重新输入");
            break;
        }
      })
          .catch(err => {
            console.log(err);         /* 若出现异常则在终端输出相关信息 */
          })
    }

  }


}
</script>

<style scoped>

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