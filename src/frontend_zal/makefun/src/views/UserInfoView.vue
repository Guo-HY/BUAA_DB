<template>
  <el-header class="el-header">
    <div>
      <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png">
      </el-avatar>
    </div>
    <div>
      {{userId}}
    </div>
  </el-header>
  <el-main>
    <el-tag
        :key="tag"
        v-for="tag in dynamicTags"
        closable
        :disable-transitions="false"
        @close="handleClose(tag)">
      {{tag}}
    </el-tag>
    <el-input
        class="input-new-tag"
        v-if="inputVisible"
        v-model="inputValue"
        ref="saveTagInput"
        size="small"
        @keyup.enter="handleInputConfirm"
        @blur="handleInputConfirm"
    >
    </el-input>
    <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>
  </el-main>
  <el-main>
    <el-descriptions class="margin-top" title="个人信息" border>
      <el-button type="primary" size="small">操作</el-button>
      <el-descriptions-item>
        <i class="el-icon-user"></i>
        用户名
        {{userName}}
      </el-descriptions-item>
      <el-descriptions-item>
        <i class="el-icon-mobile-phone"></i>
        性别
        {{gender}}
      </el-descriptions-item>
      <el-descriptions-item>
        <i class="el-icon-location-outline"></i>
        年龄
        {{age}}
      </el-descriptions-item>
      <el-descriptions-item>
        <i class="el-icon-tickets"></i>
        联系方式
        {{contact}}
      </el-descriptions-item>
      <el-descriptions-item>
        <i class="el-icon-office-building"></i>
        联系地址
        {{address}}
      </el-descriptions-item>
    </el-descriptions>
  </el-main>
</template>

<script>
export default {
  name: "UserInfoView",
  data() {
    return {
      userId : '19375203',
      userName : '流英成和',
      contact : '133xxx',
      gender : '女',
      age : '20',
      address : '北京航空航天大学',
      dynamicTags: ['标签一', '标签二', '标签三'],
      inputVisible: false,
      inputValue: ''
    };
  },
  methods: {
    handleClose(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },

    showInput() {
      this.inputVisible = true;
    },

    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.dynamicTags.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = '';
    }
  }
}
</script>

<style scoped>
.el-header{
  height: 120px;
}
.el-tag + .el-tag {
  margin-left: 30px;
}
.button-new-tag {
  margin-left: 30px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 30px;
  margin-left: 10px;
  vertical-align: bottom;
}
</style>