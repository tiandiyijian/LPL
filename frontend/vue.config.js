module.exports = {
    publicPath: "./",
    devServer: {
        proxy: {
          '/api': {
            target: 'http://127.0.0.1:8088/', //对应自己的接口
            changeOrigin: true,
            ws: true,
            secure: false,
            pathRewrite: {
              '^/api': ''
            }
          }
        }
    },
}