<template>
    <div id="home">
      <!-- <span class="deadline">截止{{ gettime }}</span> -->
      <!-- 帖子具体内容 -->
      <div>
        <!-- <el-col :span="20">
          <el-card style="margin:auto;" shadow="never">
            <el-row justify="center" align="middle" type="flex" style="font-size: 20px"> {{post_name}} </el-row>
            <el-row justify="center" style="font-size: 15px;width:1000px" > {{content}} </el-row>
          </el-card>
        </el-col> -->
        <el-row type="flex" class="row-bg" justify="center">
          
          <!-- 左半边 -->
          <el-col :span="4"><div class="grid-content bg-purple-light">
              <el-card :body-style="{ padding: '0px' }" shadow="hover">
                <el-image :src="`http://127.0.0.1:8000/${create_user_pic_path}`" ></el-image>
                <div style="padding: 14px;">
                  <a href="javascript:void(0)" onclick="gotoPro(create_user_name)">
                    <span>{{create_user_name}}</span>
                  </a>
                  <div class="bottom clearfix">
                    <time class="time">{{ post_time }}</time>
                  </div>
                </div>
              </el-card>
          </div></el-col>

          <!-- 中间 -->
          <el-col :span="11"><div class="grid-content bg-white">
            <div slot="content">
              <div class="title" style="text-align: center;" >
                {{post_name}}
              </div>
              <div>
                <time class="time">{{ likes_num }}人赞同了该帖</time>
              </div>
              </br>
              <div class="post-content">
                {{content}}
              </div>
              </div>
              <!-- 小标 -->
              <el-row style="padding: 0;margin: 0">
                <el-col :span="6">
                  <el-button type="text" style="background-color: rgba(0,132,255,.1);" @click.native="userLikePost"><i class="el-icon-caret-top"></i>赞同{{likes_num}}</el-button>

                  <!-- <el-button icon="el-icon-caret-bottom" style="color: #0084ff;background-color: rgba(0,132,255,.1);"></el-button> -->
                </el-col>

                <el-col :span="3" style="">
                  <el-button type="text" style="color: #999999;" ><i class="el-icon-message"></i>{{comment_num}} 条评论</el-button>
                </el-col>
              </el-row>
              <!-- 发起评论 -->
              <el-card class="box-card">
                <!-- 发评论人的头像 -->
                <el-row class="putcomment">
                  <el-col :span="3">
                    <!-- <div class="demo-basic--circle">
                      <div class="block"><el-avatar shape="square" :size="50" :src="squareUrl"></el-avatar></div>
                    </div> -->
                    <img class="img" :src="`http://127.0.0.1:8000/${user_pic}`"  width="50px" height="50px"></img>
                  </el-col>
                  <el-col :span="18">
                    <el-input
                      type="textarea"
                      autosize
                      placeholder="请友善评论"
                      v-model="yourcomment"
                      clearable>
                    </el-input>
                  </el-col>
                  <el-col :span="3">
                    <el-button type="primary" icon="el-icon-check" circle @click="userCreateComment"></el-button>
                  </el-col>
                </el-row>
              </el-card>
              <!-- 评论 -->
              <el-card class="box-card">
                {{comment_num}}条评论
                <el-divider></el-divider>
                <el-row v-for="item in comments" class="comment-content">
                  <el-col :span="3">
                    <!-- <div class="demo-basic--circle">
                      <div class="block"><el-avatar shape="square" :size="45" :src="squareUrl"></el-avatar></div>
                      
                    </div> -->
                    <img class="img" :src="`http://127.0.0.1:8000/${item.comment_user_pic}`"  width="50px" height="50px"></img>
                  </el-col>
                  
                <el-col :span="21">
                  <el-row style="padding: 0;margin: 0">
                    <div class="comment-font">
                      {{item.content}}
                    </div>
                  </el-row>
                  <el-row justify="end" type="flex">
                    <el-button type="danger" icon="el-icon-delete" circle size="small" @click="userDeleteComment(item.comment_id)"></el-button>
                    <el-button type="text" @click.native="userLikeComment(item.comment_id)"><i class="el-icon-caret-top"></i>赞同{{item.likes_num}}</el-button>
                  </el-row>
                  
                </el-col>

                  
                </el-row>
              </el-card>
            </div>
          </el-col>

          <!-- 右半边 -->
          <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
        </el-row>
      </div>


    </div>
    
  </template>
   
  <script>
  import qs from "qs"
  export default {
    name: "Post",
    data() {
      return {
        gettime: "", //当前时间
        postid: this.$store.state.postId,
        create_user_pic_path:"",
        user_pic:"",
        post_name : '北航期末考试大作业重叠,学生不堪重负',
        content : "",
        post_time : "2022-11-19 11:13:30",
        comment_num : 2,
        likes_num : 9999,
        create_user_name : "匿名",
        comments : [
		      {
		      	"comment_id" : 1,
		      	"content" : "学校就应该早点放我们回去,一直呆这儿人要傻了;学校就应该早点放我们回去,一直呆这儿人要傻了;学校就应该早点放我们回去,一直呆这儿人要傻了",
		      	"comment_time" : "2022-11-20 00:13:30",
		      	"likes_num" : 10000,
		      	"comment_user_id" : 2,
            comment_user_pic:""
		      },
          {
		      	"comment_id" : 2,
		      	"content" : "中传学生已经能回家了,北航什么时候能跟进;中传学生已经能回家了,北航什么时候能跟进;中传学生已经能回家了,北航什么时候能跟进;中传学生已经能回家了,北航什么时候能跟进;中传学生已经能回家了,北航什么时候能跟进;中传学生已经能回家了,北航什么时候能跟进",
		      	"comment_time" : "2022-11-20 11:12:30",
		      	"likes_num" : 3333,
		      	"comment_user_id" : 4,
            comment_user_pic:""
		      },
        ],
        // 头像
        circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
        squareUrl: "https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png",
        yourcomment:""
      };
    },
   
    methods: {
      getTime() {
      var _this = this;
        let yy = new Date().getFullYear();
        var mm =
          new Date().getMonth() > 9
            ? new Date().getMonth() + 1
            : new Date().getMonth() == 9
            ? new Date().getMonth() + 1
            : '0' + (new Date().getMonth() + 1);
        var dd = new Date().getDate() < 10 ? '0' + new Date().getDate() : new Date().getDate();
        let hh = new Date().getHours();
        let mf =
          new Date().getMinutes() < 10 ? '0' + new Date().getMinutes() : new Date().getMinutes();
        let ss =
          new Date().getSeconds() < 10 ? '0' + new Date().getSeconds() : new Date().getSeconds();
        _this.gettime = yy + '-' + mm + '-' + dd + ' ' + hh + ':' + mf + ':' + ss;
      },
      currentTime() {
        setInterval(this.getTime, 1000);
      },
      getPostInfo(){
        this.previewUserProfilePic();
        this.$http({
              method: 'post',
              url: '/api/getPostInfo',
              data: qs.stringify({
                postId:this.postid
              })
          }).then((res) => {
              console.log(res.data)
              this.post_name = res.data.post_name;
              this.content = res.data.content;
              this.post_time = res.data.post_time;
              this.comment_num = res.data.comment_num;
              this.likes_num = res.data.likes_num;
              this.create_user_name = res.data.create_user_name;
              this.comments = res.data.comments;
              this.create_user_pic_path = res.data.create_user_pic;
          })
      },
      gotoPro(name){
        console.log(name)
      },
      userLikePost(){
        console.log("yes")
        this.$http({
              method: 'post',
              url: '/api/userLikePost',
              data: qs.stringify({
                userId:this.$store.state.user_id,
                postId:this.postid
              })
          }).then((res) => {
              alert("成功点赞!")
          })
      },
      userLikeComment(id){
        console.log(id)
        this.$http({
              method: 'post',
              url: '/api/userLikeComment',
              data: qs.stringify({
                userId:this.$store.state.user_id,
                commentId:id
              })
          }).then((res) => {
              alert("点赞评论成功!")
          })
      },
      userCreateComment(){
        console.log(this.yourcomment)
        this.$http({
              method: 'post',
              url: '/api/userCreateComment',
              data: qs.stringify({
                userId:this.$store.state.user_id,
                postId:this.$store.state.postId,
                content:this.yourcomment,
                comment_time:this.gettime
              })
          }).then((res) => {
              alert("成功评论!")
          })
        this.yourcomment=""
      },
      userDeleteComment(id){
        console.log(id);
        this.$http({
              method: 'post',
              url: '/api/userDeleteComment',
              data: qs.stringify({
                userId:this.$store.state.user_id,
                commentId:id,
              })
          }).then((res) => {
            console.log(res.data)
            if (res.data.status == 'success'){
                  alert("删除成功");
                  this.getHotGroupIntro();
            }
            else{
              alert("删除失败,你无权删除此评论!")
            }
          })
      },
      previewUserProfilePic(){
        this.$http({
              method: 'post',
              url: '/api/previewUserProfilePic',
              data: qs.stringify({
                userId:this.$store.state.user_id,
              })
          }).then((res) => {
            this.user_pic = res.data.pic_path;
            console.log(res.data)
          })
      }
    },
    created() {this.getPostInfo()},
    mounted() {
      this.currentTime();
    },
  };
  </script>
   
  <style scoped>
  .title{
    font-size:20px;
    font-weight:bold;
  }
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }

  .bg-white {
    background: #f9fafc;
  }

  .bg-purple-light {
    background: #e5e9f2;
  }

  .row-bg {
    padding: 10px;
    background-color: #ffffff;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 100%;
  }

  .box-card {
    margin-top: 10px;
    width: 100%;
  }

  .comment-content{
    margin-top: 10px;
    width: 90%;
  }

  .putcomment{
    margin-top: 5px;
    width: 90%;
  }

  .comment-font{
    font-size: 13px;
    color: #90939a;
    line-height:1.7;
  }

  .post-content{
    font-size: 15px;
    margin-left: 10px;
    margin-right: 10px;
    line-height: 25px;
    margin-bottom: 10px;
  }
  </style>