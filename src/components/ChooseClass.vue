<template>
  <div>
      <el-button type="warning" size="medium">
          <a href="#/chooseclass/choose">选课</a>
      </el-button>
      <el-button type="warning" size="medium">
          <a href="#/chooseclass/withdraw">退课</a>
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
  methods: {},
  created() {},
  mounted() {}
};
</script>

<style lang="scss" scoped>

</style>