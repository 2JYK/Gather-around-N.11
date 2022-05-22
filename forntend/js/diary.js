//user id 보여주기
async function loadId() {
    console.log("here")

    const userid = await getArticles()
}
loadId()

// //게시글 보여주기(이름, 설명, 사진)
// async function loadArticles() {
//     const article = await getArticles(article_id);

//     img = article.img
//     title = article.name
//     desc = article.desc

// }

// //게시글 삭제
// async function removeArticle() {
//     await deleteArticle(article_id)

// }

// loadArticles(article_id)
