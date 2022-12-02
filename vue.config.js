module.exports = {
    devServer: {
      // 端口号
      port: 8000,
      // 配置不同的后台API地址
      proxy: {
        '/api': {
          target: 'http://127.0.0.1:8000/api/',
          ws: true,
          changeOrigin: true,
          pathRewrite: {
            '^/api': ''
          }
        }
      }
    },
    lintOnSave: false
  }