<template>
  <div >
    <div>姓名：{{ card_item.name }} </div>
      <div>学号：{{card_item.stuId}}</div>
      <div v-if="card_item.gender==1">性别：男</div>
      <div v-else>性别：女
    </div>
  </div>
</template>

<script>
export default {
  name: "Studentinfo",
  props:['card_item'],
}
</script>

<style scoped>

</style>