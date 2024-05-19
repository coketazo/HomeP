// 현재 보고있는 section 사이드바 하이라이트
window.addEventListener('scroll', () => {
	const sections = document.querySelectorAll('.content');
	let currentSectionId = '';

	// 스크롤 위치에 따라 현재 섹션을 식별
	sections.forEach(section => {
		const sectionTop = section.offsetTop;
		const sectionHeight = section.clientHeight;
		const screenHeight = window.innerHeight;
		const scrollPosition = window.scrollY;
		if (scrollPosition >= sectionTop - screenHeight / 2 && scrollPosition < sectionTop + sectionHeight - screenHeight / 2) {
			currentSectionId = section.getAttribute('id');
		}
	});

	// 현재 섹션의 링크에 active 클래스 추가
	const navLinks = document.querySelectorAll('.sidebar-nav a');
	navLinks.forEach(link => {
		link.classList.remove('active');
		if (link.getAttribute('href').substring(1) === currentSectionId) {
			link.classList.add('active');
		}
	});
});


// 사이드바 클릭시 부드러운 스크롤
document.querySelectorAll('.sidebar-nav a').forEach(anchor => {
	anchor.addEventListener('click', function (e) {
		e.preventDefault();

		const targetId = this.getAttribute('href').substring(1);
		const targetElement = document.getElementById(targetId);

		targetElement.scrollIntoView({
			behavior: 'smooth',
			block: 'center'
		});
	});
});
