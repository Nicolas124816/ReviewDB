import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';

import { AboutUsModule } from './component/main-pages/about-us/about-us.module';
import { ContactUsModule } from './component/main-pages/contact-us/contact-us.module';
import { ExampleSearchesModule } from './component/main-pages/example-searches/example-searches.module';
import { FooterModule } from './component/main-fragments/footer/footer.module';
import { HeaderModule } from './component/main-fragments/header/header.module';
import { HomeModule } from './component/main-pages/home/home.module';
import { HowItWorksModule } from './component/main-pages/how-it-works/how-it-works.module';
import { AppComponent } from './app.component';
import { CaseIconComponent } from './component/field-components/icons/case-icon/case-icon.component';

@NgModule({
  declarations: [
    AppComponent,
    CaseIconComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    AboutUsModule,
    ContactUsModule,
    ExampleSearchesModule,
    FooterModule,
    HeaderModule,
    HomeModule,
    HowItWorksModule
  ],
  bootstrap: [AppComponent],
})
export class AppModule { }
