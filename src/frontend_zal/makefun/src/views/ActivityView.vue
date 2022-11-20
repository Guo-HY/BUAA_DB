<template>
  <div>
    <el-button type="text" @click="createActivity">点击打开 Message Box</el-button>
    <div v-if="formVisible">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="活动名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="活动区域">
          <el-select v-model="form.region" placeholder="请选择活动区域">
            <el-option label="教学楼" value="新主楼"></el-option>
            <el-option label="会议室" value="咖啡厅"></el-option>
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
          <el-checkbox-group v-model="form.type">
            <el-checkbox label="线上" name="type"></el-checkbox>
            <el-checkbox label="线下" name="type"></el-checkbox>
          </el-checkbox-group>
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
  </div>
</template>

<script>
export default {
  name: "ActivityView",
  data() {
    return {
      formVisible:false,
      form: {
        userId: '',
        name: '',
        region: '',
        beginDate: '',
        endDate: '',
        activityNature: '',
        desc: '',
      }
    }
  },
  methods: {
    createActivity() {
      this.formVisible = true;
    },
    onSubmit() {
      this.$confirm('是否提交此活动', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
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

</style>