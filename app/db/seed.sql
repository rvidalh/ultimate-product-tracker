-- Insert Roles
INSERT INTO roles (name, description, is_active, created_at, updated_at) VALUES
('admin', 'Administrator with full system access', true, NOW(), NOW()),
('user', 'Regular user with basic app functionality', true, NOW(), NOW());

-- Insert Permissions
INSERT INTO permissions (name, description, resource, action, created_at, updated_at) VALUES
-- User Management
('user.create', 'Create new users', 'user', 'create', NOW(), NOW()),
('user.read', 'View user information', 'user', 'read', NOW(), NOW()),
('user.update', 'Update user information', 'user', 'update', NOW(), NOW()),
('user.delete', 'Delete users', 'user', 'delete', NOW(), NOW()),
('user.list', 'List all users', 'user', 'list', NOW(), NOW()),

-- Product Management
('product.create', 'Add new products to track', 'product', 'create', NOW(), NOW()),
('product.read', 'View product information', 'product', 'read', NOW(), NOW()),
('product.update', 'Update product information', 'product', 'update', NOW(), NOW()),
('product.delete', 'Delete products', 'product', 'delete', NOW(), NOW()),
('product.list', 'View product lists', 'product', 'list', NOW(), NOW()),

-- Web Scraping Management
('scraping.manage', 'Manage web scraping configurations', 'scraping', 'manage', NOW(), NOW()),
('scraping.execute', 'Execute web scraping tasks', 'scraping', 'execute', NOW(), NOW()),
('scraping.view_logs', 'View scraping logs and results', 'scraping', 'view_logs', NOW(), NOW()),

-- System Administration
('system.admin', 'Full system administration access', 'system', 'admin', NOW(), NOW()),
('system.settings', 'Manage system settings', 'system', 'settings', NOW(), NOW()),
('system.monitoring', 'View system monitoring and analytics', 'system', 'monitoring', NOW(), NOW()),

-- Role Management
('role.manage', 'Manage user roles and permissions', 'role', 'manage', NOW(), NOW());

-- Assign Permissions to Admin Role
INSERT INTO role_permissions (role_id, permission_id, created_at, updated_at)
SELECT r.id, p.id, NOW(), NOW()
FROM roles r
CROSS JOIN permissions p
WHERE r.name = 'admin';

-- Assign Limited Permissions to User Role
INSERT INTO role_permissions (role_id, permission_id, created_at, updated_at)
SELECT r.id, p.id, NOW(), NOW()
FROM roles r
CROSS JOIN permissions p
WHERE r.name = 'user'
AND p.name IN (
    'product.create',
    'product.read',
    'product.update',
    'product.delete',
    'product.list',
    'scraping.execute',
    'scraping.view_logs'
);