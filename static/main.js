$(function () {
	let path = window.location.pathname
	console.log(path);
	let menu_item = $(`a[href="${path}"]`);
	menu_item.next('ul').removeClass('hide');
	menu_item.parents('ul').removeClass('hide')
});
