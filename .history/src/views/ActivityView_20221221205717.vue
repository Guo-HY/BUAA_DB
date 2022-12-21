<template>
  <div>
    <el-button type="text" @click="creatingActivity">创建活动</el-button>
    <div v-if="formVisible">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="活动名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="活动区域">
          <el-select v-model="form.region" placeholder="请选择活动区域">
            <el-option label="教学楼" value="教学楼"></el-option>
            <el-option label="会议室" value="会议室"></el-option>
            <el-option label="咖啡厅" value="咖啡厅"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="活动时间">
          <el-col :span="11">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.beginDate" style="width: 100%;"></el-date-picker>
          </el-col>
          <el-col class="line" :span="2">-</el-col>
          <el-col :span="11">
            <el-time-picker placeholder="选择时间" v-model="form.endDate" style="width: 100%;"></el-time-picker>
          </el-col>
        </el-form-item>
        <el-form-item label="活动性质">
          <el-select v-model="form.type" placeholder="请选择活动形式">
            <el-option label="线上" value="线上"></el-option>
            <el-option label="线下" value="线下"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="活动描述">
          <el-input type="textarea" v-model="form.desc"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">立即创建</el-button>
          <el-button @click="cancel">取消</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div v-else>
      <el-card v-for="act in activities" :key="act" class="box-card">
        <div class="text item">
          {{'活动名称             ' + act.name}}
        </div>
        <div class="text item">
          {{'活动区域             ' + act.region}}
        </div>
        <div class="text item">
          {{'活动开始时间          ' + act.beginDate}}
        </div>
        <div class="text item">
          {{'活动性质             '+act.activityNature}}
        </div>
        <div class="text item">
          {{'活动描述             '+act.desc}}
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import qs from "qs";

export default {
  name: "ActivityView",
  data() {
    return {
      formVisible:false,
      form: {
        userId: this.$store.state.user_id,
        name: '',
        region: '',
        beginDate: '',
        endDate: '',
        activityNature: '',
        desc: '',
      },
      activities : [{
        name: '111',
        region: '222',
        beginDate: '333',
        endDate: '444',
        activityNature: '666',
        desc: '555',
      }],
    }
  },
  created() {
    this.getActivity();
  },
  methods: {
    creatingActivity() {
      this.formVisible = true;
    },
    createActivity() {
      this.$http({
        method: 'post',
        url: '/api/createActivity',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          userId: this.$store.state.user_id,
          name: this.form.name,
          region: this.form.region,
          beginDate: this.form.beginDate,
          endDate: this.form.endDate,
          activityNature: this.form.activityNature,
          desc: this.form.desc,
        })
      }).then(res => {              /* res 是 response 的缩写 */
        console.log(res.data.status);
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    },
    getActivity() {
      this.$http({
        method: 'post',
        url: '/api/getActivity',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
      }).then(res => {              /* res 是 response 的缩写 */
        console.log(res.data);
        this.activities = res.data.activities;
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    },
    onSubmit() {
      this.$confirm('是否提交此活动', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.createActivity();
        this.$message({
          type: 'success',
          message: '提交成功',
        });
        this.formVisible=false;
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消提交'
        });
      });
      this.getActivity();
    },
    cancel() {
      this.$confirm('此操作将永久删除已填信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'info',
          message: '已取消编辑',
        });
        this.formVisible=false;
      }).catch(() => {
      });
    },
  }
}


</script>

<style scoped>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
}
</style>