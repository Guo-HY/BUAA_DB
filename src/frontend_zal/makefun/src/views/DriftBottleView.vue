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
        <el-button size="small">评论</el-button>
      </el-badge>
      <el-badge :value="3" class="item">
        <el-button size="small">回复</el-button>
      </el-badge>
      <el-badge :value="1" class="item" type="primary">
        <el-button size="small">评论</el-button>
      </el-badge>
      <el-badge :value="2" class="item" type="warning">
        <el-button size="small">回复</el-button>
      </el-badge>
    </el-main>
  </el-container>

</template>

<script>
export default {
  name: "DriftBottles",
  data() {
    return {
      driftBottleContent:"你好呀",
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
</style>