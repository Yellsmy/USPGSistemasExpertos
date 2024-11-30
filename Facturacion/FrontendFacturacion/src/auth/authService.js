const usersTable = [
    {
        id: 1,
        username: 'admin',
        password: 'demo',
        email: 'admin@demo.com',
        roles: [1], // Administrator
        accessToken: 'access-token-8f3ae836da744329a6f93bf20594b5cc',
    },
    {
        id: 2,
        username: 'user',
        password: 'demo',
        email: 'user@demo.com',
        roles: [2], // operador
        accessToken: 'access-token-6829bba69dd3421d8762-991e9e806dbf',
    }
];


export function loginUser(username, password) {
    const user = usersTable.find(u => u.username === username && u.password === password);
    if (user) {
        localStorage.setItem('currentUser', JSON.stringify(user));
        window.dispatchEvent(new CustomEvent('loginSuccess')); 
        return user;
    }
    return null;
}


export function logoutUser() {
    localStorage.removeItem('currentUser');
    window.location.hash = '#login'; 
}


export function checkAuthentication() {
    return localStorage.getItem('currentUser') !== null; 
}



