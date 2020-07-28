module.exports = {
  lintOnSave: false,
  devServer: {
    disableHostCheck: true,
    proxy: {
      '/server': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: {
          '^/server': ''
        }
      }
    }
  },
  chainWebpack: config => {
    if (process.env.NODE_ENV === 'development') {
      config
        .output
        .filename('[name].[hash].js')
        .end()
    }
  },
  pwa: {
    name: '農地違章工廠',
    themeColor: '#2196f3',
    workboxOptions: {
      skipWaiting: true,
      clientsClaim: true
    }
  }
}
