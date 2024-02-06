import { NgModule } from '@angular/core';
import { AboutUsComponent } from './about-us.component';
import { HeaderModule } from '../../main-fragments/header/header.module';
import { FooterModule } from '../../main-fragments/footer/footer.module';

@NgModule({
  declarations: [
    AboutUsComponent,
  ],
  imports: [
    HeaderModule,
    FooterModule,
  ],
  exports: [
    AboutUsComponent,
  ],
})
export class AboutUsModule { }
