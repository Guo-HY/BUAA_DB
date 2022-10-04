<template>
  <div>
      <!-- <el-button type="warning" size="medium">
          <a href="#/chooseclass/choose">选课</a>
      </el-button> -->
      <!-- <el-button type="warning" size="medium">
          <a href="#/chooseclass/withdraw">退课</a>
      </el-button> -->
      <el-button href="javascript:;" @click="clickyes()" type="warning" size="medium">
        选课
      </el-button>
      <el-button href="javascript:;" @click="clickno()" type="warning" size="medium">
        退课
      </el-button>
      <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "ChooseClass",
  components: {},
  props: {},
  data() {
    return {
    };
  },
  watch: {},
  computed: {},
  methods: {
    clickyes(){
      this.$router.push("/chooseclass/choose")
    },
    clickno(){
      this.$router.push("/chooseclass/withdraw")
    }
  },
  created() {},
  mounted() {}
};
</script>

<style lang="scss" scoped>

</style>