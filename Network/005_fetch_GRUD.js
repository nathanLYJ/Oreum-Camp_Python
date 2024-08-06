// eduapi.weniv.co.kr
// 
// 30분마다 초기화되게 설계해두었어요.


// 블로그 목록 확인하기
fetch("https://eduapi.weniv.co.kr/801/blog")
  .then((response) => response.json())
  .then((json) => console.log(json))
  .catch((error) => console.error(error));
  
// 게시글 상세 정보 확인하기
fetch("https://eduapi.weniv.co.kr/801/blog/1")
  .then((response) => response.json())
  .then((json) => console.log(json))
  .catch((error) => console.error(error));

//  게시글 작성하기
fetch("https://eduapi.weniv.co.kr/801/blog", {
	method: "POST",
	headers: {
	  "Content-Type": "application/json",
	},
	body: JSON.stringify({
	  title: "test",
	  content: "test",
	}),
  })
	.then((response) => response.json())
	.then((json) => console.log(json))
	.catch((error) => console.error(error));

// 게시글 수정하기
fetch("https://eduapi.weniv.co.kr/801/blog/1", {
		method: "PUT",
		headers: {
		  "Content-Type": "application/json",
		},
		body: JSON.stringify({
		  title: "test put Nathanlyj",
		  content: "test put",
		}),
	  })
		.then((response) => response.json())
		.then((json) => console.log(json))
		.catch((error) => console.error(error));

//  게시글 삭제하기
fetch("https://eduapi.weniv.co.kr/801/blog/1", {
			method: "DELETE",
		  })
			.then((response) => response.json())
			.then((json) => console.log(json))
			.catch((error) => console.error(error));