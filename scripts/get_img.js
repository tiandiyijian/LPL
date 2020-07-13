const http = require("http");
const fs = require("fs");
const cheerio = require("cheerio")

// var img_url = "https://lpl.qq.com/es/team.shtml"
// var html_content = ""
// var images = []

const root = '../media/images/'

function save_img_fn(url, name) {
    console.log(name)
    http.get(url, (res) => {
        res.on("data", (data) => {
            fs.appendFile(root + name + ".png", data, (err) => {})
        })
    })
}


const $ = cheerio.load(fs.readFileSync('team-list.html'))

$('dl.club-bar dd a').each((idx, item) => {
    let url = 'http:' + $(item).children('img').attr('src')
    let name = $(item).children('p').text()
    save_img_fn(url, name)
})