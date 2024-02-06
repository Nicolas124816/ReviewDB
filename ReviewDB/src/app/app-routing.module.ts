import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutUsComponent } from './main-pages/about-us/about-us.component';
import { ContactUsComponent } from './main-pages/contact-us/contact-us.component';
import { ExampleSearchesComponent } from './main-pages/example-searches/example-searches.component';
import { HomeComponent } from './main-pages/home/home.component';
import { HowItWorksComponent } from './main-pages/how-it-works/how-it-works.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'about-us', component: AboutUsComponent },
  { path: 'contact-us', component: ContactUsComponent },
  { path: 'example-searches', component: ExampleSearchesComponent },
  { path: 'how-it-works', component: HowItWorksComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

