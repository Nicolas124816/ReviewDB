import { NgModule } from '@angular/core';
import { HomeComponent } from './home.component';
import { HeaderModule } from '../../main-fragments/header/header.module';
import { FooterModule } from '../../main-fragments/footer/footer.module';

@NgModule({
  declarations: [
    HomeComponent,
  ],
  imports: [
    HeaderModule,
    FooterModule,
  ],
  exports: [
    HomeComponent,
  ],
})
export class HomeModule { }
