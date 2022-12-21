<template>
  <div>
  <el-header>
    <div class="el-header">
       <div>
        <img class="img" :src="`http://127.0.0.1:8000/${pic_path}`"  width="100px" height="100px"></img>
       </div>
      <input type="file" @change="getImageFile" id="img">
      <el-button type="primary" @click="uploadUserProfilePic">确认添加</el-button>
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
        @close="handleClose(tag)">
      {{tag}}
    </el-tag>
    <el-input
        class="input-new-tag"
        v-if="inputVisible"
        v-model="inputValue"
        ref="saveTagInput"
        @keyup.enter="handleInputConfirm"
        @blur="handleInputConfirm"
    >
    </el-input>
    <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>
  </el-main>
  <el-main>
    <el-button type="primary" v-if="!changing" @click="toChangeInfo">修改信息</el-button>
    <div v-else>
      <el-button type="primary" @click="changeUserInfo">提交修改</el-button>
    </div>

    <el-descriptions class="margin-top" title="个人信息" border>
      <el-descriptions-item>
        <i class="el-icon-user"></i>
        用户名
        <el-input
            class="input-new-tag"
            v-if="changing"
            v-model="userName"
        >
        </el-input>
        <slot v-else>{{userName}}</slot>
      </el-descriptions-item>
      <el-descriptions-item>
        <i class="el-icon-mobile-phone"></i>
        性别
        <el-input
            class="input-new-tag"
            v-if="changing"
            v-model="gender"
        >
        </el-input>
        <slot v-else>{{gender}}</slot>
      </el-descriptions-item>
      <el-descriptions-item>
        <i class="el-icon-location-outline"></i>
        年龄
        <el-input
            class="input-new-tag"
            v-if="changing"
            v-model="age"
        >
        </el-input>
        <slot v-else>{{age}}</slot>
      </el-descriptions-item>
      <el-descriptions-item>
        <i class="el-icon-tickets"></i>
        联系方式
        <el-input
            class="input-new-tag"
            v-if="changing"
            v-model="contact"
        >
        </el-input>
        <slot v-else>{{contact}}</slot>
      </el-descriptions-item>
      <el-descriptions-item>
        <i class="el-icon-office-building"></i>
        联系地址
        <el-input
            class="input-new-tag"
            v-if="changing"
            v-model="address"
        >
        </el-input>
        <slot v-else>{{address}}</slot>
      </el-descriptions-item>
    </el-descriptions>
  </el-main>
</div>
</template>

<script>
import qs from "qs";
export default {
  name: "UserInfoView",
  data() {
    return {
      userId : this.$store.state.user_id,
      userName : '流英成和',
      gender : '女',
      age : '20',
      address : '北京航空航天大学',
      contact : '133xxx',
      dynamicTags: ['123', '456', '789'],
      inputVisible: false,
      changing: false,
      inputValue: '',
      pic_path:"",

    };
  },
  created() {
    this.getUserInfo();
    this.getUserTag();
    this.getUserHeadPic();
  },
  methods: {
    getImageFile:function(e) {
      let file = e.target.files[0];
      this.pic = file;
    },
    uploadUserProfilePic() {
      let formData = new FormData();
      formData.append('userId', this.$store.state.user_id);
      formData.append('pic', this.pic);
      this.$http({
        method: 'post',
        url: '/api/uploadUserProfilePic',
        data:formData
      }).then(res => {
        console.log(res.data.status);
        this.getUserHeadPic();
      }).catch(err => {
        console.log(err);
      })
    },
    handleClose(tag) {
      this.$http({
        method: 'post',
        url: '/api/userDeleteTag',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          userId : this.$store.state.user_id,
          tagName : tag,
        })
      }).then(res => {              /* res 是 response 的缩写 */
        console.log(res.data.status);
        this.getUserTag();
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
      // this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },

    showInput() {
      this.inputVisible = true;
    },
    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        // this.dynamicTags.push(inputValue);
        this.addUserTag(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = '';
    },
    getUserHeadPic() {
      this.$http({
        method: 'post',
        url: '/api/previewUserProfilePic',
        data: qs.stringify({
          userId : this.$store.state.user_id,
        })
      }).then(res => {
        this.pic_path = res.data.pic_path;
        console.log(res.data);
      }).catch(err => {
        console.log(err);
      })
    },
    getUserInfo() {
      this.$http({
        method: 'post',
        url: '/api/getUserInfo',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          userId : this.$store.state.user_id,
        })
      }).then(res => {              /* res 是 response 的缩写 */
        this.userName = res.data.userName;
        this.gender = res.data.gender;
        this.age = res.data.age;
        this.address = res.data.address;
        this.contact = res.data.contact;
        console.log(res.data);
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    },
    addUserTag(inputValue) {
      this.$http({
        method: 'post',
        url: '/api/userAddTag',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          userId : this.$store.state.user_id,
          tagName : inputValue,
        })
      }).then(res => {              /* res 是 response 的缩写 */
        console.log(res.data.status);
        this.getUserTag();
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    },
    getUserTag() {
      this.$http({
        method: 'post',
        url: '/api/getUserTag',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          userId : this.$store.state.user_id,
        })
      }).then(res => {              /* res 是 response 的缩写 */
        this.dynamicTags = res.data.dynamicTags;
        console.log(res.data);
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    },
    toChangeInfo() {
      this.changing=true;
    },
    changeUserInfo() {
      // window.alert("修改成功");
      this.changing=false;
      this.$http({
        method: 'post',
        url: '/api/changeUserInfo',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          userId : this.$store.state.user_id,
          userName : this.userName,
          gender : this.gender,
          age : this.age,
          address : this.address,
          contact : this.contact,
        })
      }).then(res => {              /* res 是 response 的缩写 */
        switch (res.data.status) {
          case "success":
            window.alert("修改成功");
            break;
          case "fail":
            window.alert("修改失败");
            break;
        }
        console.log(res.data);
        this.getUserInfo();
      }).catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    }
  }
}
</script>

<style scoped>
.el-header{
  height: 800px;
}
.el-tag + .el-tag {
  margin-left: 40px;
  height: 32px;
}
.button-new-tag {
  margin-left: 20px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 120px;
  margin-left: 10px;
  vertical-align: bottom;
}
</style>