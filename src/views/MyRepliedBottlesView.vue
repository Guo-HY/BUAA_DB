<template>
  <div>
    <el-collapse v-model="activeNames" @change="handleChange">
      <el-collapse-item v-for="bot in bottles" :key="bot"  title="点击查看详情">
        <div>{{bot.content}}</div>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
import qs from "qs";

export default {
  name: "MyRepliedBottlesView",
  data() {
    return {
      bottles:[],
    };
  },
  created() {
    this.getMyRepliedBottles();
  },
  methods: {
    handleChange(val) {
      console.log(val);
    },
    getMyRepliedBottles() {
      this.$http({
        method: 'post',
        url: '/api/getMyRepliedBottles',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          userId: this.$store.state.user_id,
        })
      }).then(res => {              /* res 是 response 的缩写 */
        console.log(res.data);
        this.bottles=res.data.bottles;
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    }

  }
}
</script>

<style scoped>

</style>