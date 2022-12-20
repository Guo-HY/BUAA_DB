<template>
  <div>
    <el-collapse>
      <el-collapse-item v-for="reply in bottlesAndReplys" :key=reply  title="点击查看详情">
        <div>{{'回复者id'+reply.replyUserId}}</div>
        <div>{{reply.reply}}
          <el-button v-if="reply.acc" type="primary" size="small">已赞同</el-button>
          <el-button v-if="reply.acc" type="info" icon="el-icon-user-solid" circle></el-button>
          <el-button v-if="!reply.acc" type="primary" size="small" @click="agreeWithReply(reply)">赞同</el-button>
        </div>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
import qs from "qs";
export default {
  name: "MyReceivedBottleReplysView",
  data() {
    return {
      bottlesAndReplys:[
        {content : '', reply : '', replyUserId : '', acc : false}
      ],
    };
  },
  created() {
    this.getMyReceivedBottleReplys();
  },
  methods: {
    handleChange(val) {
      console.log(val);
    },
    getMyReceivedBottleReplys() {
      this.$http({
        method: 'post',
        url: '/api/getMyReceivedBottleReplys',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          userId: this.$store.state.user_id,
        })
      }).then(res => {              /* res 是 response 的缩写 */
        console.log(res.data);
        this.bottlesAndReplys=res.data.bottlesAndReplys;
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    },
    agreeWithReply(reply) {
      reply.acc=true;
      console.log(reply);
    }

  }
}
</script>

<style scoped>

</style>