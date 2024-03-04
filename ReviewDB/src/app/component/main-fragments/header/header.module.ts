import { NgModule } from '@angular/core';
import { HeaderComponent } from './header.component';
import { HomeIconModule } from '../../field-components/icons/home-icon/home-icon.module'
import { InfoIconModule } from '../../field-components/icons/info-icon/info-icon.module'
import { MailIconModule } from '../../field-components/icons/mail-icon/mail-icon.module'
import { QuestionIconModule } from '../../field-components/icons/question-icon/question-icon.module'
import { SearchIconModule } from '../../field-components/icons/search-icon/search-icon.module'
import { TeamIconModule } from '../../field-components/icons/team-icon/team-icon.module'
import { ToolsIconModule } from '../../field-components/icons/tools-icon/tools-icon.module'

@NgModule({
  declarations: [
    HeaderComponent,
  ],
  imports: [
    HomeIconModule,
    InfoIconModule,
    MailIconModule,
    QuestionIconModule,
    SearchIconModule,
    TeamIconModule,
    ToolsIconModule
  ],
  exports: [
    HeaderComponent,
  ],
})
export class HeaderModule { }
