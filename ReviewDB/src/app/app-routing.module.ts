import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutUsComponent } from './component/main-pages/about-us/about-us.component';
import { ContactUsComponent } from './component/main-pages/contact-us/contact-us.component';
import { ExampleSearchesComponent } from './component/main-pages/example-searches/example-searches.component';
import { HomeComponent } from './component/main-pages/home/home.component';
import { HowItWorksComponent } from './component/main-pages/how-it-works/how-it-works.component';
import { ProjectLinksComponent } from './component/main-pages/project-links/project-links.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'about-us', component: AboutUsComponent },
  { path: 'contact-us', component: ContactUsComponent },
  { path: 'example-searches', component: ExampleSearchesComponent },
  { path: 'how-it-works', component: HowItWorksComponent },
  { path: 'project-links', component: ProjectLinksComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

