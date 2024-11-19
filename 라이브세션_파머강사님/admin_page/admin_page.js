// 카테고리 데이터
const category_data = [
    { id: 1, category: "전체 상품" },
    { id: 2, category: "상의" },
    { id: 3, category: "하의" },
    { id: 4, category: "신발" },
    { id: 5, category: "패션잡화" },
    // ...
];

// 카테고리 선택 박스에 옵션 추가
const category_data_table = document.getElementsByName('category_data_table')[0];

category_data.forEach(item => {
    const option = document.createElement('option');
    option.value = item.id; // id를 옵션의 값으로 설정
    option.text = item.category;  // option 요소에 사용될 글자
    category_data_table.add(option);
});

// 제품 데이터
const product_data = [
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' },
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000' },
    { category: "신발", brand: 'Nike', product: '에어포스 1', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
    { category: "차마", brand: '몰라', product: '찢어진 치마', price: '500,,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
    // ...
];

// 제품 테이블에 데이터 추가
const product_data_Table = document.getElementById('product_data_Table');

// 초기 데이터 로딩
function loadProductData(filteredData) {
    product_data_Table.innerHTML = ''; // 기존 테이블 데이터 초기화
    filteredData.forEach(item => {
        const row = product_data_Table.insertRow();
        row.insertCell(0).innerHTML = item.category;
        row.insertCell(1).innerHTML = item.brand;
        row.insertCell(2).innerHTML = item.product;
        row.insertCell(3).innerHTML = item.price;
    });
}

// 검색 버튼 클릭 이벤트
document.querySelector('.btn').addEventListener('click', function() {
    const selectedCategory = category_data_table.value; // 선택된 카테고리 값
    const searchTerm = document.getElementById('autoSizingInput').value.toLowerCase(); // 검색어

    let filteredData = product_data;

    // 조건별 상태 변화 이벤트

    // 전체 상품 선택 후 검색어 입력하지 않고 검색
    if (selectedCategory == 1 && searchTerm === '') {
        filteredData = product_data; // 모든 제품 표시
    }
    // 전체 상품 선택 후 검색어 입력 시
    else if (selectedCategory == 1 && searchTerm !== '') {
        filteredData = product_data.filter(item => item.product.toLowerCase().includes(searchTerm));
    }
    // 카테고리 선택 후 검색어 입력하지 않고 검색
    else if (selectedCategory && searchTerm === '') {
        filteredData = product_data.filter(item => item.category === category_data.find(cat => cat.id == selectedCategory).category);
    }
    // 카테고리 선택과 검색어 입력 시
    else if (selectedCategory && searchTerm !== '') {
        filteredData = product_data.filter(item => 
            item.category === category_data.find(cat => cat.id == selectedCategory).category && 
            item.product.toLowerCase().includes(searchTerm)
        );
    }
    // 카테고리 선택하지 않고 검색어만 입력 시
    else if (!selectedCategory && searchTerm !== '') {
        filteredData = product_data.filter(item => item.product.toLowerCase().includes(searchTerm));
    }

    // 필터링된 데이터 로드
    loadProductData(filteredData);
});

// 초기 데이터 로딩
loadProductData(product_data);
