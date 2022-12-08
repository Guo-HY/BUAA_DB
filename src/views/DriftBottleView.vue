<template>
  <el-container>
    <el-header>
      欢迎来到漂流瓶
    </el-header>
    <el-main>
      <div class="bottleBox">
        {{driftBottleContent}}
      </div>
    </el-main>
    <el-main>
      <el-badge :value="12" class="item">
        <el-button size="small" @click="redirectMySendDriftBottles">我发出的漂流瓶</el-button>
      </el-badge>
      <el-badge :value="3" class="item">
        <el-button size="small" @click="redirectMyReceivedBottleReplys">我收到的漂流瓶回复</el-button>
      </el-badge>
      <el-badge :value="1" class="item" type="primary">
        <el-button size="small" @click="redirectMyRepliedBottles">我回复的漂流瓶</el-button>
      </el-badge>
<!--      <el-badge :value="2" class="item" type="warning">-->
<!--        <el-button size="small">我认可的漂流瓶的回复</el-button>-->
<!--      </el-badge>-->
    </el-main>
    <el-main>
      <el-input
          type="textarea"
          :rows="8"
          placeholder="请输入漂流瓶内容"
          v-model="sendText"
          class="sendBox">
      </el-input>
      <div>
        <el-button type="success" round>发送漂流瓶</el-button>
      </div>
    </el-main>
  </el-container>

</template>

<script>
import qs from "qs";

export default {
  name: "DriftBottles",
  data() {
    return {
      driftBottleContent:"你好呀",
      myText:"",
    }
  },
  created() {
    this.getOneRandomDriftBottleContent();
  },
  methods: {
    getOneRandomDriftBottleContent() {
      this.$http({
        method: 'post',
        url: '/api/getOneRandomDriftBottleContent',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          userId: this.$store.state.user_id,
        })
      }).then(res => {              /* res 是 response 的缩写 */
        console.log(res.data);
        this.driftBottleContent=res.data.content;
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    },
    redirectMyRepliedBottles() {
      this.$router.push("MyRepliedBottles")
    },
    redirectMyReceivedBottleReplys() {
      this.$router.push("MyReceivedBottleReplys")
    },
    redirectMySendDriftBottles() {
      this.$router.push("MySendDriftBottles")
    },
    sendText() {
      this.$http({
        method: 'post',
        url: '/api/sendText',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          userId: this.$store.state.user_id,
          content: this.myText,
        })
      }).then(res => {              /* res 是 response 的缩写 */
        console.log(res.data);
        this.myText='';
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    }
  }
}
</script>

<style scoped>
.item {
  margin-top: 10px;
  margin-right: 40px;
}

.bottleBox{
  height: 200px;
  background-color: #30B7A5;
}

.sendBox{
  height: 200px;
  background-color: #8FE6DA;
}
</style>