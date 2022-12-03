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
                <el-image :src="'https://source.unsplash.com/random'" ></el-image>
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

                  <el-button icon="el-icon-caret-bottom" style="color: #0084ff;background-color: rgba(0,132,255,.1);"></el-button>
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
                    <div class="demo-basic--circle">
                      <div class="block"><el-avatar shape="square" :size="50" :src="squareUrl"></el-avatar></div>
                    </div>
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
                    <div class="demo-basic--circle">
                      <div class="block"><el-avatar shape="square" :size="45" :src="squareUrl"></el-avatar></div>
                      
                    </div>
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
        post_name : '北航期末考试大作业重叠,学生不堪重负',
        content : "   特别赞同楼上一个朋友的回答：北航的氛围不对。我是一直在学院路，学院路校区给我整体的感觉也是压抑。大家好像都很忙，很自私，很冷漠，只顾自己拼命卷。以我们班为例，我是个小专业，班里30几个人为了争几个保研名额互相勾心斗角，尔虞我诈。给课代表交个作业都要担心会不会被故意改错，问问同学基物实验有什么注意事项压根不告诉你，甚至故意挖坑让你跳。班里几个班干部自成一派，把本专业的资源几乎垄断，不好的事情指使你去做，好的事情不跟你说。同学几年，一点感情都没有。再说说其他，感觉学院路校区人的总体素质不高。表白墙上啥事都能引战，宿舍楼道里凌晨一两点吹头发打电话的多的是，进楼道时前面的同学不但不帮忙扶下门，还很有可能往你脸上甩帘子，教室里用电脑发出不小动静的也不在少数。这些都是小事，但让我很不舒服。相比之下，我总感觉沙河的小伙伴善良热心，每次去沙河时都舍不得离开。至于学业……大一大二不少课是公共基础课还好，大二下学期专业课开始，明显感觉课程质量和课程设置也太糟糕了吧。老师上课纯粹在水，念PPT的还算好的，有的老师把课程资料一发就看自己的电脑去了（线下上课，来教室的目的就是往讲台上一坐）。从大一到大三课表排得满满的，我这个专业连三年暑假都排上课了，大四上学期还有综合实验，相当于小型毕业设计，压根不给考研人留活路。课多也就算了，主要是大部分课其实真的都没什么用啊，稀里糊涂学了一大堆，到头来一场空。以上，北航绝对配不上它的高考分数线，也就是沾了在北京的光了。我自己已经被困住了，后悔也没什么用了。看到不少朋友评论，我说明一下：我不是六系的，是个非大类招生的边缘工科，专业人数在全校几乎都算是最少的。毕业即失业的专业，依然那么卷。这两天又发生了不少事情，简直刷新了我对学院和同学的认识。现在只能在此告诉大家一句：千万千万不要来我这个专业！除非你的父母是大学老师/三甲医院医生/从政，或者你想直接躺平，或者你的学习能力真的特别特别强，普通平民千万不要来这个专业！你会被当成傻子玩弄四年。学院路的风气是不好，但我这个专业估计是全校最差的，大学几年可是见识到什么叫做精致的利己主义者了。在这里说可能没什么用了，希望高中生可以看见吧。实话说，我觉得北航总体上还是可以的，后悔的主要是这个专业，不是学校。上北航尽量学传统的专业吧，别学那些小门小类，新专业尤其注意。我认识的其他学院的朋友都没有像我们班这样，我的描述也只是展现了北航那么多人中的极小一部分，很多人不了解的极小一部分。当然也有同学夸我们这个专业的，但那是受益者，是佼佼者，对于我这样的普通人来说体验感十分不好。最后祝大家在北航开开心心每一天！",
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
		      	"comment_user_id" : 2
		      },
          {
		      	"comment_id" : 2,
		      	"content" : "中传学生已经能回家了,北航什么时候能跟进;中传学生已经能回家了,北航什么时候能跟进;中传学生已经能回家了,北航什么时候能跟进;中传学生已经能回家了,北航什么时候能跟进;中传学生已经能回家了,北航什么时候能跟进;中传学生已经能回家了,北航什么时候能跟进",
		      	"comment_time" : "2022-11-20 11:12:30",
		      	"likes_num" : 3333,
		      	"comment_user_id" : 4
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