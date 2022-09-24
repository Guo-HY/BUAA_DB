<template>
  <div>
      <h1>可选课程列表</h1>
      <el-table
            :data="classes"
            stripe
            style="width: 100%">
            <template v-for="(item,index) in headArr">
                console.log(index)
                <el-table-column :key="index" v-if="item.ind===5" :label="item.label" align="center">
                    <el-button href="javascript:;" @click="clickchoose" type="text" size="small">选择</el-button>
                    <!-- <template v-for="(cls,index) in classes">
                        
                    </template> -->
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
  name: "ChooseYes",
  components: {},
  props: {},
  data() {
    return {
        classes:[
            {name:"oo", id:"1", num:"100", info:"面向对象,圣杯之战"},
            {name:"os", id:"2", num:"100", info:"操作系统,抄就行"},
            {name:"co", id:"3", num:"100", info:"计组,祭祖"},
            {name:"intro to ai", id:"4", num:"100", info:"人工智能引论,水课"}
        ],
        headArr:[
            {label:'课程名称', prop:"name", ind:1},
            {label:'课程编号', prop:"id", ind:2},
            {label:'课程介绍' , prop : 'info', ind:3},
            {label:'剩余人数' , prop : 'num', ind:4},
            {label:'操作', ind:5}
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
      clickchoose(id){
          console.log(id)
          alert("选课成功"); 
          this.$http.post("url").then((res) => {
              
              
          })
      }
  },
  created() {
      this.find();
  },
  mounted() {}
};
</script>

<style lang="scss" scoped>

</style>