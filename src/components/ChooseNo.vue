<template>
  <div>
    <el-table
            :data="classes"
            stripe
            style="width: 100%">
            <template v-for="(item,index) in headArr">
                console.log(index)
                <el-table-column :key="index" v-if="item.ind===4" :label="item.label" align="center">
                    <el-button href="javascript:;" @click="clickwithdraw" type="text" size="small">退选</el-button>
                </el-table-column>
                <el-table-column :key="index" v-else :prop="item.prop" :label="item.label" align="center">
                    <template scope="scope">
                        <span>
                            {{scope.row[item.prop]}}
                        </span>
                    </template>
                </el-table-column>
            </template>    
        </el-table>
  </div>
</template>

<script>
export default {
  name: "ChooseNo",
  components: {},
  props: {},
  data() {
    return {
      classes:[
            {name:"oo", id:"1", num:"4"},
            {name:"os", id:"2", num:"5"},
            {name:"co", id:"3", num:"6"},
            {name:"intro to ai", id:"4", num:"100"}
        ],
      headArr:[
          {label:'课程名称', prop:"name", ind:1},
          {label:'课程编号', prop:"id", ind:2},
          {label:'剩余人数' , prop : 'num', ind:3},
          {label:'操作', ind:4}
      ]
    };
  },
  watch: {},
  computed: {},
  methods: {
    find(){
          this.$http.get("url").then((res) => {
              console.log(res.data.classes)
              this.classes = res.data.classes
          })
    },
    clickwithdraw(id){
          console.log(id)
          alert("退课成功"); 
          this.$router.push("/chooseclass") // 切换路由
          this.$http.post("url").then((res) => {
            
            
          })
      }
  },
  created() {},
  mounted() {}
};
</script>

<style lang="scss" scoped>

</style>