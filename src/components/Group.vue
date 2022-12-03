<template>
  <div>
    <span class="deadline">当前时间{{ gettime }}</span>
    <div class="pic_table">
      <img class="img" :src="'https://source.unsplash.com/random'"  width="100px" height="100px"></img>
      <infoaddr>{{gpname}}</infoaddr>
      <postnum>{{"关注 : "+post_num}}</postnum>
      <tagsaddr>
        {{"标签 : "}}
        <template v-for="item in tags">
          <el-tag>{{item}}</el-tag> &#12288
        </template>
      </tagsaddr>
      <tagsedit>
        <el-button type="primary" icon="el-icon-edit" size="small" @click="userAddTagToGroup"></el-button>
        
      </tagsedit>
      <tagseditcontent>
        <el-input v-model="usertag" placeholder="输入想添加的tag" clearable></el-input>
      </tagseditcontent>
    </div>

    <!-- 添加帖子 -->
    <el-button type="text" @click="dialog = true">发起帖子</el-button>
    <el-drawer
    title="同学,请填写必要信息来发起帖子"
    :before-close="userCreatePost"
    :visible.sync="dialog"
    direction="ltr"
    custom-class="demo-drawer"
    ref="drawer"
    >
        <div class="demo-drawer__content">
          <el-form :model="form">
            <el-form-item label="帖子名称" :label-width="formLabelWidth">
              <el-input v-model="form.name" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="帖子内容" :label-width="formLabelWidth">
              <el-input type="textarea" autosize v-model="form.context" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div class="demo-drawer__footer">
            <el-button @click="cancelForm">取 消</el-button>
            <el-button type="primary" @click="$refs.drawer.closeDrawer()"     :loading="loading">{{ loading ? '提交中 ...' : '确 定' }}</el-button>
        </div>
      </div>
    </el-drawer>
    
    <!-- 帖子 -->
    <div class="zhihu-item-class" v-for="(item,index) in posts">
      <el-row>
        <h3 style="float: left;margin-left: 10px" @click="intoPost(item.post_id )">{{item.post_name}}</h3>
      </el-row>
      <el-row style="margin-top: 10px;padding: 10px">
        <el-col :span="3">      <el-image :src="'https://source.unsplash.com/random'" style="width: 100px; height: 100px"></el-image>
        </el-col> 
        <el-col :span="15">
        <!-- <folder >Dr.粲: 赵慧婵是我同班同学,下午热搜第二的时候班级群久违的热闹了起来。说起来我了解的我们班在清华/中科院系统中已经有三位博导了,都是30岁左右从国外被引进的,而赵慧婵无疑是其中最优秀的一位。其实我个…</folder> -->
        <el-collapse >
          <el-collapse-item title="展开">
            <div>{{item.context}}</div>
          </el-collapse-item>
        </el-collapse>
        
        </el-col>
      </el-row>
      <el-row style="padding: 0;margin: 0">
        <el-col :span="6">
          <el-button style="color: #0084ff;background-color: rgba(0,132,255,.1);"><i class="el-icon-caret-top"></i>赞同 {{item.likes_num}}</el-button>
          <el-button icon="el-icon-caret-bottom" style="color: #0084ff;background-color: rgba(0,132,255,.1);"></el-button>
        </el-col>
        <el-row>
          <el-col :span="3" style="">

            <el-button type="text" style="color: #999999;"><i class="el-icon-message"></i>{{item.comment_num}} 条评论</el-button>
          </el-col>
          <el-col :span="2" style="">          <el-button type="text" style="color: #999999;"><i class="el-icon-share"></i>分享</el-button>
          </el-col>
          <el-col :span="2" style="">
            <el-button type="text" style="color: #999999;"><i class="el-icon-star-on"></i>收藏</el-button>
          </el-col>
          <el-col :span="2" style="">
            <el-button type="text" style="color: #999999;"><i class="el-icon-heavy-rain"></i>喜欢</el-button>
          </el-col>
          <el-col :span="2">
            <el-dropdown  style="padding: 10px">
              <i class="el-icon-more"></i>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item>没有帮助</el-dropdown-item>
                <el-dropdown-item>举报</el-dropdown-item>
                <el-dropdown-item>不感兴趣</el-dropdown-item>
              </el-dropdown-menu>

            </el-dropdown>

          </el-col>
          <!-- <el-col :span="3" style="">
            <el-button type="text"> <i class="el-icon-arrow-up"></i>收起</el-button>
          </el-col> -->
        </el-row>

      </el-row>
      </div>

    

  </div>
</template>

<script>
import qs from "qs"
export default {
  name: "Group",
  components: {},
  props: {},
  data() {
    return {
        user_id:this.$store.state.user_id,
        groupId:this.$store.state.groupId,
        gpname:'LOL',
        gp_desc:'网游巅峰',
        post_num:2,
        create_user_name:'zlb',
        tags:['MOBA'],
        gettime:"",
        usertag:'',
        form: {
          name: '',
          context: ''
        },
        dialog: false,
        loading: false,
        formLabelWidth: '80px',
        timer: null,
        posts:[
          {
            "post_id" : 1,
			      "post_name" : "DRX夺冠引热议,Deft最后一舞泪洒赛场",
			      "context" : "详细略",
            "post_time" : "2022-11-16 21:44:30",
            "comment_num" : 2,
            "likes_num" : 999,
            "create_user_name" : "ghy"
          },
          {
            "post_id" : 2,
			      "post_name" : "北航期末考试大作业重叠,学生不堪重负",
			      "context" : "详细略",
            "post_time" : "2022-11-19 11:13:30",
            "comment_num" : 999,
            "likes_num" : 9999,
            "create_user_name" : "匿名"
          },
        ]
    };
  },
  watch: {},
  computed: {},
  methods: {
    getAll(){
        this.$http({
              method: 'post',
              url: '/api/getGroupInfo',
              data: qs.stringify({
                groupId:this.groupId
              })
          }).then((res) => {
              console.log(res.data)
              this.gpname = res.data.group_name;
              this.gp_desc = res.data.group_description;
              this.post_num = res.data.post_num;
              this.create_user_name = res.data.create_user_name;
              this.tags = res.data.tags;
              this.posts = res.data.posts;
          })
      },
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
      userAddTagToGroup(){
        console.log(this.usertag)
        this.$http({
              method: 'post',
              url: '/userAddTagToGroup',
              data: qs.stringify({
                userId:this.user_id,
                groupId:this.groupId,
                tagName:this.usertag
              })
          }).then((res) => {
              this.tags.push(this.usertag)
              this.usertag = ""
              alert("添加成功!")
          })
      },
      userCreatePost(done){
        if (this.loading) {
          return;
        }
        this.$confirm('确定要提交表单吗？')
        .then(_ => {
          this.loading = true;
          this.timer = setTimeout(() => {
            done();
          //   this.$http({
          //     method: 'post',
          //     url: '/userCreatePost',
          //     data: qs.stringify({
          //       userId:this.user_id,
          //       groupId:this.groupId,
          //       post_name:this.form.name,
          //       context:this.form.context,
          //       post_time:this.gettime
          //     })
          // }).then((res) => {
          //     alert("评论成功!")
          // })

            
            // 动画关闭需要一定的时间
            setTimeout(() => {
                this.loading = false;
              }, 400);
            }, 2000);
            console.log(this.form)
        })
        .catch(_ => {});
        
      },
      cancelForm() {
        this.loading = false;
        this.dialog = false;
        clearTimeout(this.timer);
      },
      intoPost(id){
        console.log(id)
        this.$store.commit("setPostid",id)
        this.$router.push("/post")
      }
  },
  created() {this.getAll()},
  mounted() {
      this.currentTime();
  },
};
</script>

<style lang="scss" scoped>
  .pic_table {
    position: relative;
    width: 1000px;
    height: 200px;
  }

  .pic_table infoaddr {
    position: absolute;
    left: 120px;
    bottom: 100px;
  }

  .pic_table postnum {
    position: absolute;
    left: 200px;
    bottom: 100px;
  }

  .pic_table tagsaddr {
    position: absolute;
    left: 700px;
    bottom: 100px;
  }

  .pic_table tagsedit {
    position: absolute;
    left: 300px;
    bottom: 100px;
  }

  .pic_table tagseditcontent {
    position: absolute;
    left: 350px;
    bottom: 100px;
  }
</style>