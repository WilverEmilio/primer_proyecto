/**
* This code was generated by v0 by Vercel.
* @see https://v0.dev/t/ctkHGOaLYbi
* Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
*/

/** Add fonts into your Next.js project:

import { Archivo } from 'next/font/google'

archivo({
  subsets: ['latin'],
  display: 'swap',
})

To read more about using these font, please visit the Next.js documentation:
- App Directory: https://nextjs.org/docs/app/building-your-application/optimizing/fonts
- Pages Directory: https://nextjs.org/docs/pages/building-your-application/optimizing/fonts
**/
'use client';
import { useRouter } from 'next/navigation'; // Hook de Next.js para la navegación
import { useState } from 'react';
import Link from "next/link";
import { DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem, DropdownMenuSeparator } from "@/components/ui/dropdown-menu";
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar";
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "@/components/ui/card";
import PresentacionPage from '@/app/presentacion/page';
import CategoriaPage from '@/app/categoria/page';
import EmpleadoPage from '@/app/empleado/page';
import ClientePage from '@/app/cliente/page';
import ProveedorPage from '@/app/proveedor/page';

export function Dashboard() {
  const [selectedSection, setSelectedSection] = useState('home');

  const handleMenuClick = (section) => {
    setSelectedSection(section);
  };

  return (
    <div className="flex flex-col min-h-screen">
      <header className="bg-primary text-primary-foreground py-4 px-6 flex items-center justify-between">
        <nav className="flex items-center gap-4">
          <Link
            href="#"
            className="px-4 py-2 rounded-md hover:bg-primary/80 transition-colors"
            onClick={() => handleMenuClick('home')}
          >
            Home
          </Link>
          <DropdownMenu>
            <DropdownMenuTrigger className="px-4 py-2 rounded-md hover:bg-primary/80 transition-colors flex items-center">
              Products
              <ChevronDownIcon className="w-4 h-4 ml-2" />
            </DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuItem onClick={() => handleMenuClick('articles')}>
                <Link href="#" prefetch={false}>
                  Articles
                </Link>
              </DropdownMenuItem>
              <DropdownMenuItem onClick={() => handleMenuClick('categories')}>
                <Link href="#" prefetch={false}>
                  Categorias
                </Link>
              </DropdownMenuItem>
              <DropdownMenuItem onClick={() => handleMenuClick('presentations')}>
                <Link href="#" prefetch={false}>
                  Presentations
                </Link>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
          <DropdownMenu>
            <DropdownMenuTrigger className="px-4 py-2 rounded-md hover:bg-primary/80 transition-colors flex items-center">
              Suppliers
              <ChevronDownIcon className="w-4 h-4 ml-2" />
            </DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuItem onClick={() => handleMenuClick('buy-products')}>
                <Link href="#" prefetch={false}>
                  Buy Products
                </Link>
              </DropdownMenuItem>
              <DropdownMenuItem onClick={() => handleMenuClick('supplier-list')}>
                <Link href="#" prefetch={false}>
                  Proveedor
                </Link>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
          <DropdownMenu>
            <DropdownMenuTrigger className="px-4 py-2 rounded-md hover:bg-primary/80 transition-colors flex items-center">
              Users
              <ChevronDownIcon className="w-4 h-4 ml-2" />
            </DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuItem onClick={() => handleMenuClick('employees')}>
                <Link href="#" prefetch={false}>
                  Empleados
                </Link>
              </DropdownMenuItem>
              <DropdownMenuItem onClick={() => handleMenuClick('customers')}>
                <Link href="#" prefetch={false}>
                  Customers
                </Link>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
          <Link
            href="#"
            className="px-4 py-2 rounded-md hover:bg-primary/80 transition-colors"
            onClick={() => handleMenuClick('clients')}
          >
            Clientes
          </Link>
          <DropdownMenu>
            <DropdownMenuTrigger className="px-4 py-2 rounded-md hover:bg-primary/80 transition-colors flex items-center">
              Invoices
              <ChevronDownIcon className="w-4 h-4 ml-2" />
            </DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuItem onClick={() => handleMenuClick('reports')}>
                <Link href="#" prefetch={false}>
                  Reports
                </Link>
              </DropdownMenuItem>
              <DropdownMenuItem onClick={() => handleMenuClick('bills')}>
                <Link href="#" prefetch={false}>
                  Bills
                </Link>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </nav>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Avatar className="h-10 w-10">
              <AvatarImage src="/placeholder-user.jpg" alt="User Avatar" />
              <AvatarFallback>JD</AvatarFallback>
            </Avatar>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuItem>My Account</DropdownMenuItem>
            <DropdownMenuItem>Settings</DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem>Logout</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </header>
      <main className="flex-1 bg-background p-8">
        {selectedSection === 'home' && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <Card>
              <CardHeader>
                <CardTitle>Total Products</CardTitle>
                <CardDescription>The total number of products in the store.</CardDescription>
              </CardHeader>
              <CardContent className="flex items-center justify-center text-4xl font-bold">
                <span>1,234</span>
              </CardContent>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle>Active Suppliers</CardTitle>
                <CardDescription>The number of active suppliers.</CardDescription>
              </CardHeader>
              <CardContent className="flex items-center justify-center text-4xl font-bold">
                <span>78</span>
              </CardContent>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle>Registered Users</CardTitle>
                <CardDescription>The total number of registered users.</CardDescription>
              </CardHeader>
              <CardContent className="flex items-center justify-center text-4xl font-bold">
                <span>456</span>
              </CardContent>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle>Active Clients</CardTitle>
                <CardDescription>The number of active clients.</CardDescription>
              </CardHeader>
              <CardContent className="flex items-center justify-center text-4xl font-bold">
                <span>321</span>
              </CardContent>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle>Pending Invoices</CardTitle>
                <CardDescription>The number of pending invoices.</CardDescription>
              </CardHeader>
              <CardContent className="flex items-center justify-center text-4xl font-bold">
                <span>89</span>
              </CardContent>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle>Total Revenue</CardTitle>
                <CardDescription>The total revenue for the store.</CardDescription>
              </CardHeader>
              <CardContent className="flex items-center justify-center text-4xl font-bold">
                <span>$987,654</span>
              </CardContent>
            </Card>
          </div>
        )}
        {selectedSection === 'categories' && (
          <div>
            <CategoriaPage />
          </div>
        )}
        {selectedSection === 'presentations' && (
          <div>
            <PresentacionPage />
          </div>
        )}
        {selectedSection === 'buy-products' && (
          <div>
            <h2>Buy Products</h2>
            {/* Contenido de "Buy Products" aquí */}
          </div>
        )}
        {selectedSection === 'supplier-list' && (
          <div>
            <ProveedorPage />
          </div>
        )}
        {selectedSection === 'employees' && (
          <div>
            <EmpleadoPage />
          </div>
        )}
        {selectedSection === 'customers' && (
          <div>
            <h2>Customers</h2>
            {/* Contenido de "Customers" aquí */}
          </div>
        )}
        {selectedSection === 'clients' && (
          <div>
            <ClientePage />
          </div>
        )}
        {selectedSection === 'reports' && (
          <div>
            <h2>Reports</h2>
            {/* Contenido de "Reports" aquí */}
          </div>
        )}
        {selectedSection === 'bills' && (
          <div>
            <h2>Bills</h2>
            {/* Contenido de "Bills" aquí */}
          </div>
        )}
      </main>
      <footer className="bg-muted text-muted-foreground py-4 px-6 flex items-center justify-between">
        <div>&copy; 2023 Acme Grocery Store</div>
        <div>
          <Link href="#" className="hover:text-primary transition-colors" prefetch={false}>
            Terms of Service
          </Link>
          <span className="mx-2">|</span>
          <Link href="#" className="hover:text-primary transition-colors" prefetch={false}>
            Privacy Policy
          </Link>
        </div>
      </footer>
    </div>
  );
}

function ChevronDownIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round">
      <path d="m6 9 6 6 6-6" />
    </svg>
  );
}
