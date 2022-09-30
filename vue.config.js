const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  configureWebpack: {
    devServer: {
      proxy: {
        "/api": {//捕获API的标志，如果API中有这个字符串，那么就开始匹配代理，
          target: "http://127.0.0.1:8000/api/",//代理的api地址，就是要跨域的地址
          changeOrigin: true,// 这个参数可以让target参数是域名
          ws: true,//是否启用websockets，用不到可设为false
          pathRewrite: {//对路径匹配到的字符串重写
            "^/api": "",
          },
        },
      },
    },
  },
})
